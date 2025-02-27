from concurrent.futures import Future
from unittest import mock

import pytest

from tiktorch.server.session.backend import commands as cmds


class TestCommandQueue:
    def test_stop_command_has_higher_priorityj(self):
        cmd_queue = cmds.CommandPriorityQueue()
        stop_cmd = cmds.ShutdownCmd()
        cmd_queue.put_nowait(cmds.ResumeTrainingCmd())
        cmd_queue.put_nowait(stop_cmd)
        cmd_queue.put_nowait(cmds.PauseTrainingCmd())

        received_cmd = cmd_queue.get_nowait()
        assert stop_cmd is received_cmd

    def test_queue_order_is_stable(self):
        cmd_queue = cmds.CommandPriorityQueue()
        stop_cmds = [cmds.ShutdownCmd() for _ in range(100)]
        for cmd in stop_cmds:
            cmd_queue.put_nowait(cmd)

        for expected_cmd in stop_cmds:
            assert expected_cmd is cmd_queue.get_nowait()


class TestForwardPassCmd:
    class FailException(Exception):
        pass

    def test_cmd_accepts_future_as_constructor_arg(self):
        fut = Future()
        cmds.ForwardPass(fut, [1])

    def test_executing_resolves_future(self):
        fut = Future()

        cmd = cmds.ForwardPass(fut, [1])
        ctx = cmds.Context(supervisor=mock.Mock())
        cmd.execute(ctx)

        assert fut.result()

    def test_executing_resolves_future_if_raised(self):
        fut = Future()
        cmd = cmds.ForwardPass(fut, [1])
        supervisor = mock.Mock()
        supervisor.forward.side_effect = self.FailException("fail")

        ctx = cmds.Context(supervisor=supervisor)
        cmd.execute(ctx)

        with pytest.raises(self.FailException):
            assert fut.result()
