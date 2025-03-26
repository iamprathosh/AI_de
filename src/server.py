import grpc
from concurrent import futures
import logging

# Import the generated classes
import federated_pb2
import federated_pb2_grpc

# Define the server class
class FederatedLearningServer(federated_pb2_grpc.FederatedLearningServicer):

    def __init__(self):
        self.model_updates = []

    def SendModelUpdate(self, request, context):
        try:
            self.model_updates.append(request.model_update)
            logging.info("Received model update")
            return federated_pb2.ModelUpdateResponse(status="Success")
        except Exception as e:
            logging.error(f"Error receiving model update: {e}")
            return federated_pb2.ModelUpdateResponse(status="Failure")

    def GetModelUpdates(self, request, context):
        try:
            for update in self.model_updates:
                yield federated_pb2.ModelUpdate(model_update=update)
            logging.info("Sent model updates")
        except Exception as e:
            logging.error(f"Error sending model updates: {e}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    federated_pb2_grpc.add_FederatedLearningServicer_to_server(FederatedLearningServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()
