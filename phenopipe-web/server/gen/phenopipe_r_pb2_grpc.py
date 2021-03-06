# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import phenopipe_pb2 as phenopipe__pb2
import phenopipe_r_pb2 as phenopipe__r__pb2


class PhenopipeRStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PostprocessAnalysis = channel.unary_unary(
        '/phenopipe.PhenopipeR/PostprocessAnalysis',
        request_serializer=phenopipe__r__pb2.PostprocessRequest.SerializeToString,
        response_deserializer=phenopipe__pb2.JobResponse.FromString,
        )
    self.FetchPostprocessingResult = channel.unary_unary(
        '/phenopipe.PhenopipeR/FetchPostprocessingResult',
        request_serializer=phenopipe__pb2.FetchJobResultRequest.SerializeToString,
        response_deserializer=phenopipe__r__pb2.PostprocessResponse.FromString,
        )
    self.UploadPostprocessingStack = channel.unary_unary(
        '/phenopipe.PhenopipeR/UploadPostprocessingStack',
        request_serializer=phenopipe__r__pb2.UploadPostprocessingStackRequest.SerializeToString,
        response_deserializer=phenopipe__r__pb2.UploadPostprocessingStackResponse.FromString,
        )
    self.DeletePostprocessingStack = channel.unary_unary(
        '/phenopipe.PhenopipeR/DeletePostprocessingStack',
        request_serializer=phenopipe__r__pb2.DeletePostprocessingStackRequest.SerializeToString,
        response_deserializer=phenopipe__r__pb2.DeletePostprocessingStackResponse.FromString,
        )
    self.GetPostprocessingStack = channel.unary_unary(
        '/phenopipe.PhenopipeR/GetPostprocessingStack',
        request_serializer=phenopipe__r__pb2.GetPostprocessingStackRequest.SerializeToString,
        response_deserializer=phenopipe__r__pb2.GetPostprocessingStackResponse.FromString,
        )
    self.GetPostprocessingStacks = channel.unary_unary(
        '/phenopipe.PhenopipeR/GetPostprocessingStacks',
        request_serializer=phenopipe__r__pb2.GetPostprocessingStacksRequest.SerializeToString,
        response_deserializer=phenopipe__r__pb2.GetPostprocessingStacksResponse.FromString,
        )


class PhenopipeRServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PostprocessAnalysis(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchPostprocessingResult(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadPostprocessingStack(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePostprocessingStack(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPostprocessingStack(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPostprocessingStacks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PhenopipeRServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PostprocessAnalysis': grpc.unary_unary_rpc_method_handler(
          servicer.PostprocessAnalysis,
          request_deserializer=phenopipe__r__pb2.PostprocessRequest.FromString,
          response_serializer=phenopipe__pb2.JobResponse.SerializeToString,
      ),
      'FetchPostprocessingResult': grpc.unary_unary_rpc_method_handler(
          servicer.FetchPostprocessingResult,
          request_deserializer=phenopipe__pb2.FetchJobResultRequest.FromString,
          response_serializer=phenopipe__r__pb2.PostprocessResponse.SerializeToString,
      ),
      'UploadPostprocessingStack': grpc.unary_unary_rpc_method_handler(
          servicer.UploadPostprocessingStack,
          request_deserializer=phenopipe__r__pb2.UploadPostprocessingStackRequest.FromString,
          response_serializer=phenopipe__r__pb2.UploadPostprocessingStackResponse.SerializeToString,
      ),
      'DeletePostprocessingStack': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePostprocessingStack,
          request_deserializer=phenopipe__r__pb2.DeletePostprocessingStackRequest.FromString,
          response_serializer=phenopipe__r__pb2.DeletePostprocessingStackResponse.SerializeToString,
      ),
      'GetPostprocessingStack': grpc.unary_unary_rpc_method_handler(
          servicer.GetPostprocessingStack,
          request_deserializer=phenopipe__r__pb2.GetPostprocessingStackRequest.FromString,
          response_serializer=phenopipe__r__pb2.GetPostprocessingStackResponse.SerializeToString,
      ),
      'GetPostprocessingStacks': grpc.unary_unary_rpc_method_handler(
          servicer.GetPostprocessingStacks,
          request_deserializer=phenopipe__r__pb2.GetPostprocessingStacksRequest.FromString,
          response_serializer=phenopipe__r__pb2.GetPostprocessingStacksResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'phenopipe.PhenopipeR', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
