import dataclasses
import io
import multiprocessing as _mp
import uuid
import zipfile
from concurrent.futures import Future
from multiprocessing.connection import Connection
from typing import List, Optional, Tuple

import numpy

from tiktorch import log
from tiktorch.rpc import Shutdown
from tiktorch.rpc import mp as _mp_rpc
from tiktorch.rpc.mp import MPServer
from bioimageio.core import load_resource_description

from .backend import base
from .rpc_interface import IRPCModelSession


@dataclasses.dataclass
class ModelInfo:
    # TODO: Test for model info
    name: str
    input_axes: str
    output_axes: str
    valid_shapes: List[List[Tuple[str, int]]]
    halo: List[Tuple[str, int]]
    offset: List[Tuple[str, int]]
    scale: List[Tuple[str, float]]


class ModelSessionProcess(IRPCModelSession):
    def __init__(self, model_zip: bytes, devices: List[str]) -> None:
        with zipfile.ZipFile(io.BytesIO(model_zip)) as model_file:
            self._model = load_resource_description(model_file, devices)

        self._datasets = {}
        self._worker = base.SessionBackend(self._model)

    def forward(self, input_tensors: numpy.ndarray) -> Future:
        res = self._worker.forward(input_tensors)
        return res

    def create_dataset(self, mean, stddev):
        id_ = uuid.uuid4().hex
        self._datasets[id_] = {"mean": mean, "stddev": stddev}
        return id_

    def get_model_info(self) -> ModelInfo:
        return ModelInfo(
            self._model.name,
            self._model.input_axes,
            self._model.output_axes,
            valid_shapes=[self._model.input_shape],
            halo=self._model.halo,
            scale=self._model.scale,
            offset=self._model.offset,
        )

    def shutdown(self) -> Shutdown:
        self._worker.shutdown()
        return Shutdown()


def _run_model_session_process(
    conn: Connection, model_zip: bytes, devices: List[str], log_queue: Optional[_mp.Queue] = None
):
    try:
        # from: https://github.com/pytorch/pytorch/issues/973#issuecomment-346405667
        import resource

        rlimit = resource.getrlimit(resource.RLIMIT_NOFILE)
        resource.setrlimit(resource.RLIMIT_NOFILE, (4096, rlimit[1]))
    except ModuleNotFoundError:
        pass  # probably running on windows

    if log_queue:
        log.configure(log_queue)

    session_proc = ModelSessionProcess(model_zip, devices)
    srv = MPServer(session_proc, conn)
    srv.listen()


def start_model_session_process(
    model_zip: bytes, devices: List[str], log_queue: Optional[_mp.Queue] = None
) -> Tuple[_mp.Process, IRPCModelSession]:
    client_conn, server_conn = _mp.Pipe()
    proc = _mp.Process(
        target=_run_model_session_process,
        name="ModelSessionProcess",
        kwargs={"conn": server_conn, "devices": devices, "log_queue": log_queue, "model_zip": model_zip},
    )
    proc.start()
    return proc, _mp_rpc.create_client(IRPCModelSession, client_conn)
