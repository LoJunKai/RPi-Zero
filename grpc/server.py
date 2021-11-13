from concurrent import futures
import logging, os

import grpc
import example_pb2
import example_pb2_grpc
import json

jsonPath = "serverJson"

class Greeter(example_pb2_grpc.GreeterServicer):

    def __init__(self):
        serverName = ""

    # Initial greeting
    def InitiateConnection(self, request, context):
        self.serverName = input("Server name: ")
        return example_pb2.replyMessage(message='Connected to server: '.format(request.name))
    
    # Choose what server is to do
    def ServerFunction(self, request, context):
        option = input("0: Send JSON\n1: Receive Data\n")
        return example_pb2.replyMessage(message = option)

    # Data sent by server
    def serverSend(self, request, context):
        f = open(jsonPath)
        data = json.load(f)
        return example_pb2.data(payload = json.dumps(data), title = self.serverName)

    # Data sent by client
    def clientSend(self, request, context):
        data = json.loads(request.payload)
        with open(os.path.join(jsonPath, "{}.json".format(request.title)), 'w') as f:
            json.dump(data, f, indent=4)
        return example_pb2.replyMessage(message="{} received data".format(self.serverName))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()