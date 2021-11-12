from concurrent import futures
import logging

import grpc
import example_pb2
import example_pb2_grpc
import json

class Greeter(example_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print(json.loads(request.name))
        return example_pb2.HelloReply(message=json.dumps({'hello':'test'}))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()