from __future__ import print_function
import argparse
import json
import logging
from config import *
import hybrid_pb2
import hybrid_pb2_grpc
import grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hybrid_pb2_grpc.GreeterStub(channel)
        response = stub.InitiateConnection(hybrid_pb2.requestMessage(name='sensor'))
        print(response.message)

        f = open(TEST_FILE)
        data = json.load(f)

        reply = stub.SendPayload(hybrid_pb2.data(
            payload=json.dumps(data), title="{}".format('sensor')))

        print("{}".format(reply.message))


if __name__ == '__main__':
    logging.basicConfig()
    run()
