from concurrent import futures
import logging, os

import grpc
import example_pb2
import example_pb2_grpc
import json

import argparse

parser = argparse.ArgumentParser(description='Server process for gRPC')
parser.add_argument('--name', metavar='n', type=str,
                    help='name of server')

args = parser.parse_args()

jsonPath = "serverJson"

class Greeter(example_pb2_grpc.GreeterServicer):

    # Initial greeting
    def InitiateConnection(self, request, context):
        print(f'Incoming connection from {request.name}')
        return example_pb2.replyMessage(message='Connected to server: {}'.format(args.name))
    
    # Data sent by client
    def SendPayload(self, request, context):
        data = json.loads(request.payload)
        with open(os.path.join(jsonPath, "{}.json".format(request.title)), 'w') as f:
            json.dump(data, f, indent=4)
        title = request.title
        title = title.split('_')
        print(f'Client sent data: {int(title[0]) + 1}')
        return example_pb2.replyMessage(message="{} received data".format(args.name))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()