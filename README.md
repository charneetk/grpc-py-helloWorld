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

1.  Create a .env file:
    You must create a .env file in the root directory of the project to define the required environment variables. The script uses DROOLS_API_URL to communicate with the Drools API.

2.  Ensure Drools is Running:
    This script assumes the Drools API is running at the URL specified in DROOLS_API_URL. Make sure Drools is set up correctly and that it is running on the specified URL

3.  Once the server is running, navigate to the client/ directory and run the client to send a request to the server:
    python client.py

4.  Input Prompt:
    The script will prompt you for two inputs:

            Message Text: Enter the message text you want to verify with Drools.
            Message Status: Enter the status for the message. Valid values are NEW or PROCESSED

5.  Drools API Call:
    The script will send the provided message text and status to the Drools API for validation. If the rule is verified (i.e., the status returned is PROCESSED), it proceeds to make a gRPC call.

6.  gRPC Call:
    If the Drools rule is verified successfully, the script proceeds to call a gRPC service (SayHello), passing the message text as the name parameter. The response from the gRPC service is printed.

# Expected Output

When the client successfully connects to the server, the output should be:

Greeter client received: Hello, <>!
