import unittest
import grpc
from src.client import FederatedLearningClient
import federated_pb2
import federated_pb2_grpc

class TestFederatedLearningClient(unittest.TestCase):

    def setUp(self):
        self.client = FederatedLearningClient('localhost:50051')

    def test_send_model_update(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = federated_pb2_grpc.FederatedLearningStub(channel)
            request = federated_pb2.ModelUpdate(model_update="test_update")
            response = stub.SendModelUpdate(request)
            self.assertEqual(response.status, "Success")

    def test_get_model_updates(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = federated_pb2_grpc.FederatedLearningStub(channel)
            request = federated_pb2.ModelUpdateRequest()
            responses = stub.GetModelUpdates(request)
            updates = [response.model_update for response in responses]
            self.assertIn("test_update", updates)

    def test_send_model_update_error_handling(self):
        with self.assertRaises(grpc.RpcError):
            self.client.send_model_update(None)

    def test_get_model_updates_error_handling(self):
        with self.assertRaises(grpc.RpcError):
            self.client.get_model_updates()

if __name__ == '__main__':
    unittest.main()
