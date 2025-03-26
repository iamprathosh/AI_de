import grpc
import logging

# Import the generated classes
import federated_pb2
import federated_pb2_grpc

class FederatedLearningClient:

    def __init__(self, server_address):
        self.server_address = server_address
        self.channel = grpc.insecure_channel(self.server_address)
        self.stub = federated_pb2_grpc.FederatedLearningStub(self.channel)

    def send_model_update(self, model_update):
        try:
            request = federated_pb2.ModelUpdate(model_update=model_update)
            response = self.stub.SendModelUpdate(request)
            logging.info(f"Send model update response: {response.status}")
        except Exception as e:
            logging.error(f"Error sending model update: {e}")

    def get_model_updates(self):
        try:
            request = federated_pb2.ModelUpdateRequest()
            for response in self.stub.GetModelUpdates(request):
                logging.info(f"Received model update: {response.model_update}")
        except Exception as e:
            logging.error(f"Error receiving model updates: {e}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    client = FederatedLearningClient('localhost:50051')
    # Example usage
    client.send_model_update("example_model_update")
    client.get_model_updates()
