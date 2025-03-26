import unittest
import grpc
from concurrent import futures
from src.server import FederatedLearningServer
import federated_pb2
import federated_pb2_grpc

class TestFederatedLearningServer(unittest.TestCase):

    def setUp(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        federated_pb2_grpc.add_FederatedLearningServicer_to_server(FederatedLearningServer(), self.server)
        self.server.add_insecure_port('[::]:50051')
        self.server.start()
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = federated_pb2_grpc.FederatedLearningStub(self.channel)

    def tearDown(self):
        self.server.stop(None)
        self.channel.close()

    def test_send_model_update(self):
        request = federated_pb2.ModelUpdateRequest(model_update="test_update")
        response = self.stub.SendModelUpdate(request)
        self.assertEqual(response.status, "Success")

    def test_get_model_updates(self):
        request = federated_pb2.ModelUpdateRequest(model_update="test_update")
        self.stub.SendModelUpdate(request)
        responses = self.stub.GetModelUpdates(federated_pb2.Empty())
        updates = [response.model_update for response in responses]
        self.assertIn("test_update", updates)

    def test_send_model_update_error_handling(self):
        with self.assertRaises(grpc.RpcError):
            request = federated_pb2.ModelUpdateRequest(model_update=None)
            self.stub.SendModelUpdate(request)

    def test_get_model_updates_error_handling(self):
        with self.assertRaises(grpc.RpcError):
            responses = self.stub.GetModelUpdates(None)
            for response in responses:
                pass

if __name__ == '__main__':
    unittest.main()
