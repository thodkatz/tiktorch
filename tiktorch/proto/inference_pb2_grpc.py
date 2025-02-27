# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import inference_pb2 as inference__pb2
from . import utils_pb2 as utils__pb2


class InferenceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateModelSession = channel.unary_unary(
                '/inference.Inference/CreateModelSession',
                request_serializer=inference__pb2.CreateModelSessionRequest.SerializeToString,
                response_deserializer=utils__pb2.ModelSession.FromString,
                )
        self.CloseModelSession = channel.unary_unary(
                '/inference.Inference/CloseModelSession',
                request_serializer=utils__pb2.ModelSession.SerializeToString,
                response_deserializer=utils__pb2.Empty.FromString,
                )
        self.CreateDatasetDescription = channel.unary_unary(
                '/inference.Inference/CreateDatasetDescription',
                request_serializer=inference__pb2.CreateDatasetDescriptionRequest.SerializeToString,
                response_deserializer=inference__pb2.DatasetDescription.FromString,
                )
        self.GetLogs = channel.unary_stream(
                '/inference.Inference/GetLogs',
                request_serializer=utils__pb2.Empty.SerializeToString,
                response_deserializer=inference__pb2.LogEntry.FromString,
                )
        self.ListDevices = channel.unary_unary(
                '/inference.Inference/ListDevices',
                request_serializer=utils__pb2.Empty.SerializeToString,
                response_deserializer=utils__pb2.Devices.FromString,
                )
        self.Predict = channel.unary_unary(
                '/inference.Inference/Predict',
                request_serializer=utils__pb2.PredictRequest.SerializeToString,
                response_deserializer=utils__pb2.PredictResponse.FromString,
                )


class InferenceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateModelSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseModelSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDatasetDescription(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLogs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDevices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InferenceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateModelSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateModelSession,
                    request_deserializer=inference__pb2.CreateModelSessionRequest.FromString,
                    response_serializer=utils__pb2.ModelSession.SerializeToString,
            ),
            'CloseModelSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseModelSession,
                    request_deserializer=utils__pb2.ModelSession.FromString,
                    response_serializer=utils__pb2.Empty.SerializeToString,
            ),
            'CreateDatasetDescription': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDatasetDescription,
                    request_deserializer=inference__pb2.CreateDatasetDescriptionRequest.FromString,
                    response_serializer=inference__pb2.DatasetDescription.SerializeToString,
            ),
            'GetLogs': grpc.unary_stream_rpc_method_handler(
                    servicer.GetLogs,
                    request_deserializer=utils__pb2.Empty.FromString,
                    response_serializer=inference__pb2.LogEntry.SerializeToString,
            ),
            'ListDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDevices,
                    request_deserializer=utils__pb2.Empty.FromString,
                    response_serializer=utils__pb2.Devices.SerializeToString,
            ),
            'Predict': grpc.unary_unary_rpc_method_handler(
                    servicer.Predict,
                    request_deserializer=utils__pb2.PredictRequest.FromString,
                    response_serializer=utils__pb2.PredictResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'inference.Inference', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Inference(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateModelSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inference.Inference/CreateModelSession',
            inference__pb2.CreateModelSessionRequest.SerializeToString,
            utils__pb2.ModelSession.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseModelSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inference.Inference/CloseModelSession',
            utils__pb2.ModelSession.SerializeToString,
            utils__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDatasetDescription(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inference.Inference/CreateDatasetDescription',
            inference__pb2.CreateDatasetDescriptionRequest.SerializeToString,
            inference__pb2.DatasetDescription.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLogs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/inference.Inference/GetLogs',
            utils__pb2.Empty.SerializeToString,
            inference__pb2.LogEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inference.Inference/ListDevices',
            utils__pb2.Empty.SerializeToString,
            utils__pb2.Devices.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inference.Inference/Predict',
            utils__pb2.PredictRequest.SerializeToString,
            utils__pb2.PredictResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class FlightControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/inference.FlightControl/Ping',
                request_serializer=utils__pb2.Empty.SerializeToString,
                response_deserializer=utils__pb2.Empty.FromString,
                )
        self.Shutdown = channel.unary_unary(
                '/inference.FlightControl/Shutdown',
                request_serializer=utils__pb2.Empty.SerializeToString,
                response_deserializer=utils__pb2.Empty.FromString,
                )


class FlightControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Shutdown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FlightControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=utils__pb2.Empty.FromString,
                    response_serializer=utils__pb2.Empty.SerializeToString,
            ),
            'Shutdown': grpc.unary_unary_rpc_method_handler(
                    servicer.Shutdown,
                    request_deserializer=utils__pb2.Empty.FromString,
                    response_serializer=utils__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'inference.FlightControl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FlightControl(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inference.FlightControl/Ping',
            utils__pb2.Empty.SerializeToString,
            utils__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Shutdown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/inference.FlightControl/Shutdown',
            utils__pb2.Empty.SerializeToString,
            utils__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
