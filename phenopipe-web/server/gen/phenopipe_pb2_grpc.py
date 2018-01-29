# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import phenopipe_pb2 as phenopipe__pb2


class PhenopipeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.WatchJob = channel.unary_stream(
        '/phenopipe.Phenopipe/WatchJob',
        request_serializer=phenopipe__pb2.WatchJobRequest.SerializeToString,
        response_deserializer=phenopipe__pb2.ProgressResponse.FromString,
        )


class PhenopipeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def WatchJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PhenopipeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'WatchJob': grpc.unary_stream_rpc_method_handler(
          servicer.WatchJob,
          request_deserializer=phenopipe__pb2.WatchJobRequest.FromString,
          response_serializer=phenopipe__pb2.ProgressResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'phenopipe.Phenopipe', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))