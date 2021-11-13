from __future__ import print_function

import logging
import os

import grpc
import example_pb2
import example_pb2_grpc
import json

jsonPath = "clientJson"


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = example_pb2_grpc.GreeterStub(channel)
        clientName = input("Please input client name: ")
        response = stub.InitiateConnection(example_pb2.requestMessage(name=clientName))


        # Server choice
        response = stub.ServerFunction(example_pb2.requestMessage(name=clientName))
        choice = response.message

        # Server sending JSON data over
        if str(choice) == "0":
            res = stub.serverSend(example_pb2.requestMessage(name=clientName))
            data = json.loads(res.payload)

            with open(os.path.join(jsonPath, "{}.json".format(res.title)), 'w') as f:
                json.dump(data, f, indent=4)
            print("JSON file received")

        # Client sending data
        elif str(choice) == "1":
            f = open(os.path.join(jsonPath, "cMsg.json"))
            data = json.load(f)

            number = input("Please input the number of times you want the data to be sent: ")
            count = 0

            while count < int(number):
                reply = stub.clientSend(example_pb2.data(payload=json.dumps(data), title="{}_{}".format(count,clientName)))
                count += 1
                print("{}: {}".format(count,reply))

        print("Finished sending {} packets".format(number))

if __name__ == '__main__':
    logging.basicConfig()
    run()
