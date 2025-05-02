import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import grpc
from concurrent import futures
from generated import helloWorld_pb2_grpc
from greeter import Greeter

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloWorld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
