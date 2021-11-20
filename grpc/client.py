from __future__ import print_function

from util import Profiler
from config import *

import logging
import os

import grpc
import example_pb2
import example_pb2_grpc
import json

import argparse

p = Profiler()

parser = argparse.ArgumentParser(description='Client process for gRPC')
parser.add_argument('--name', metavar='n', type=str,
                    help='name of client')
parser.add_argument('--times', metavar='t', type=int,
                    help='times to send json payload')

args = parser.parse_args()

jsonPath = "clientJson"

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = example_pb2_grpc.GreeterStub(channel)
        response = stub.InitiateConnection(example_pb2.requestMessage(name=args.name))
        print(response.message)

        f = open(os.path.join(jsonPath, "cMsg.json"))
        data = json.load(f)
        count = 0

        # t = Thread(target=thread_log, args=(os.getpid(),))
        # t.start()
        p.start_log()
        while count < int(args.times):
            reply = stub.SendPayload(example_pb2.data(payload=json.dumps(data), title="{}_{}".format(count,args.name)))
            count += 1
            print("{}: {}".format(reply.message, count))
            # print(f"{psutil.net_io_counters().bytes_sent}")

        print("Finished sending {} packets".format(args.times))
        # t.do_run = False
        p.end_log()

if __name__ == '__main__':
    logging.basicConfig()
    run()
