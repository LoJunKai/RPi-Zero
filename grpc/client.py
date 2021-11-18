from __future__ import print_function

# Add import path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

import argparse
import json
import logging

from testing.config import *
from testing.util import Profiler

import example_pb2
import example_pb2_grpc
import grpc


parser = argparse.ArgumentParser(description='Client process for gRPC')
parser.add_argument('-n', '--name', metavar='n', type=str, required=True,
                    help='name of client')
parser.add_argument('-t', '--times', metavar='t', type=int, required=True,
                    help='times to send json payload')

args = parser.parse_args()


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    p = Profiler()

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = example_pb2_grpc.GreeterStub(channel)
        response = stub.InitiateConnection(example_pb2.requestMessage(name=args.name))
        print(response.message)

        f = open(TEST_FILE1)
        data = json.load(f)
        count = 0

        # t = Thread(target=thread_log, args=(os.getpid(),))
        # t.start()
        p.start_log()
        while count < args.times:
            reply = stub.SendPayload(example_pb2.data(
                payload=json.dumps(data), title="{}_{}".format(count, args.name)))
            count += 1
            print("{}: {}".format(reply.message, count))
            # print(f"{psutil.net_io_counters().bytes_sent}")

        print("Finished sending {} packets".format(args.times))
        # t.do_run = False
        p.end_log()


if __name__ == '__main__':
    logging.basicConfig()
    if args.times <= 0:
        raise argparse.ArgumentTypeError("Please input a positive integer for --times.")
    run()
