import grpc
import hybrid_pb2
import hybrid_pb2_grpc
import json
from concurrent import futures
import paho.mqtt.publish as publish
from pathlib import Path
from config import *
import _thread

class Greeter(hybrid_pb2_grpc.GreeterServicer):

    # Initial greeting
    def InitiateConnection(self, request, context):
        print(f'Incoming connection from {request.name}')
        return hybrid_pb2.replyMessage(message='Connected to server: {}'.format("Server"))

    # Data sent by client
    def SendPayload(self, request, context):
        data = json.loads(request.payload)
        with open(Path(STORE_DATA, f"{request.title}.json"), 'w') as f:
            json.dump(data, f, indent=4)
        print(f'Client sent data: {data}\nPublishing to subscribers')
        _thread.start_new_thread(mqtt_pub, (data,))
        return hybrid_pb2.replyMessage(message="{} stored data and sent to subscriber".format("Server"))

def mqtt_pub(data):
    publish.single(TOPIC, json.dumps(data), hostname="localhost")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hybrid_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()