import argparse
import json
import logging
from pathlib import Path
from concurrent import futures

import example_pb2
import example_pb2_grpc
import grpc

parser = argparse.ArgumentParser(description='Server process for gRPC')
parser.add_argument('-n', '--name', metavar='n', type=str, required=True,
                    help='name of server')

args = parser.parse_args()

jsonPath = Path(Path(__file__).parent, "serverJson")


class Greeter(example_pb2_grpc.GreeterServicer):

    # Initial greeting
    def InitiateConnection(self, request, context):
        print(f'Incoming connection from {request.name}')
        return example_pb2.replyMessage(message='Connected to server: {}'.format(args.name))

    # Data sent by client
    def SendPayload(self, request, context):
        data = json.loads(request.payload)
        with open(Path(jsonPath, f"{request.title}.json"), 'w') as f:
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
    Path(jsonPath).mkdir(exist_ok=True)
    serve()
