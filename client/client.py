import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import grpc
import generated.helloWorld_pb2 as helloWorld_pb2
import generated.helloWorld_pb2_grpc as helloWorld_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloWorld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloWorld_pb2.HelloRequest(name='Codeblock'))
    print(f"Greeter client received: {response.message}")

if __name__ == '__main__':
    run()
