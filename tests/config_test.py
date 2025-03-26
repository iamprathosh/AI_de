import unittest
from src.config import Config

class TestConfig(unittest.TestCase):

    def test_grpc_settings(self):
        self.assertEqual(Config.GRPC_SERVER_ADDRESS, 'localhost:50051')
        self.assertEqual(Config.GRPC_MAX_WORKERS, 10)

    def test_ipfs_settings(self):
        self.assertEqual(Config.IPFS_ADDRESS, '/dns/localhost/tcp/5001/http')

    def test_serverless_settings(self):
        self.assertEqual(Config.AWS_REGION, 'us-east-1')
        self.assertEqual(Config.TRAINING_FUNCTION_NAME, 'my_training_function')

    def test_security_settings(self):
        self.assertEqual(Config.ENCRYPTION_KEY, 'your_encryption_key')
        self.assertEqual(Config.JWT_SECRET, 'your_jwt_secret')

    def test_fault_tolerance_settings(self):
        self.assertEqual(Config.NODE_ADDRESSES, ['localhost:50051', 'localhost:50052'])

    def test_environment_variable_support(self):
        import os
        os.environ['GRPC_SERVER_ADDRESS'] = 'test_address'
        os.environ['GRPC_MAX_WORKERS'] = '5'
        os.environ['IPFS_ADDRESS'] = 'test_ipfs_address'
        os.environ['AWS_REGION'] = 'test_region'
        os.environ['TRAINING_FUNCTION_NAME'] = 'test_function'
        os.environ['ENCRYPTION_KEY'] = 'test_encryption_key'
        os.environ['JWT_SECRET'] = 'test_jwt_secret'
        os.environ['NODE_ADDRESSES'] = 'test_address1,test_address2'

        self.assertEqual(Config.GRPC_SERVER_ADDRESS, 'test_address')
        self.assertEqual(Config.GRPC_MAX_WORKERS, 5)
        self.assertEqual(Config.IPFS_ADDRESS, 'test_ipfs_address')
        self.assertEqual(Config.AWS_REGION, 'test_region')
        self.assertEqual(Config.TRAINING_FUNCTION_NAME, 'test_function')
        self.assertEqual(Config.ENCRYPTION_KEY, 'test_encryption_key')
        self.assertEqual(Config.JWT_SECRET, 'test_jwt_secret')
        self.assertEqual(Config.NODE_ADDRESSES, ['test_address1', 'test_address2'])

if __name__ == '__main__':
    unittest.main()
