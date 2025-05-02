# gRPC Hello World Example

This project demonstrates a simple **gRPC** server and client setup, using **Python**. The server provides a greeting service, and the client sends a request to the server and receives a response.

## Prerequisites

- Python 3.7 or higher
- pip version 9.0.1 or higher
- grpcio
- grpcio-tools

To install the required Python packages, run:

```bash
pip install grpcio grpcio-tools

```

## Setup and Running the Application

1. Generate gRPC Python Files if not present

Before running the server and client, you need to generate the gRPC Python files from the .proto file. This can be done using the grpcio-tools package.

Run the following command from the root directory of the project:
python -m grpc_tools.protoc -I=proto --python_out=generated --grpc_python_out=generated proto/helloWorld.proto

# Run the Server

    Navigate to the server/ directory and start the gRPC server by running:
    python server.py

The server will start and listen on port 50051 for incoming gRPC requests.

# Run the Client

Once the server is running, navigate to the client/ directory and run the client to send a request to the server:
python client.py

The client will send a HelloRequest with the name "World" and print the server's response.

# Expected Output

When the client successfully connects to the server, the output should be:

Greeter client received: Hello, World!
