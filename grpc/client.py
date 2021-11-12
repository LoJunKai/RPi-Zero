from __future__ import print_function

import logging

import grpc
import example_pb2
import example_pb2_grpc
import json

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = example_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(example_pb2.HelloRequest(name=json.dumps({'test':'message'})))
        print(json.loads(response.message))

if __name__ == '__main__':
    logging.basicConfig()
    run()