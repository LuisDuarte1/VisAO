"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import main_pb2 as main__pb2

class VisAOStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetImages = channel.unary_unary('/visao.VisAO/GetImages', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=main__pb2.Image.FromString)
        self.UploadFile = channel.unary_unary('/visao.VisAO/UploadFile', request_serializer=main__pb2.FileUpload.SerializeToString, response_deserializer=main__pb2.File.FromString)

class VisAOServicer(object):
    """Interface exported by the server.
    """

    def GetImages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_VisAOServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetImages': grpc.unary_unary_rpc_method_handler(servicer.GetImages, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=main__pb2.Image.SerializeToString), 'UploadFile': grpc.unary_unary_rpc_method_handler(servicer.UploadFile, request_deserializer=main__pb2.FileUpload.FromString, response_serializer=main__pb2.File.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('visao.VisAO', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class VisAO(object):
    """Interface exported by the server.
    """

    @staticmethod
    def GetImages(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/visao.VisAO/GetImages', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, main__pb2.Image.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/visao.VisAO/UploadFile', main__pb2.FileUpload.SerializeToString, main__pb2.File.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)