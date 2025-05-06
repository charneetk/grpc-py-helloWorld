import os
import sys
import requests
import grpc
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generated import helloWorld_pb2
from generated import helloWorld_pb2_grpc

DROOLS_API_URL = os.getenv("DROOLS_API_URL")


def verify_rule(message_text, message_status):
    payload = {
        "text": message_text,
        "status": message_status
    }

    try:
        response = requests.post(DROOLS_API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        print(f"Processed message: {result['text']}, Status: {result['status']}")
        return result.get('status')
    except requests.RequestException as e:
        print(f"Error calling Drools API: {e}")
        return None


def run():
    message_text = input("Enter the message text: ")
    message_status = input("Enter the message status (NEW/PROCESSED): ")

    status = verify_rule(message_text, message_status)
    if status == "PROCESSED":
        print("\nDrools rule verified. Proceeding to call gRPC service...")

        channel = grpc.insecure_channel('localhost:50051')
        stub = helloWorld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloWorld_pb2.HelloRequest(name=message_text))
        print(f"Greeter client received: {response.message}")
    else:
        print("\nDrools rule verification failed or rule not matched. Aborting gRPC call.")


if __name__ == '__main__':
    run()
