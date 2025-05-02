from generated import helloWorld_pb2, helloWorld_pb2_grpc

class Greeter(helloWorld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloWorld_pb2.HelloReply(message=f"Hello, {request.name}!")