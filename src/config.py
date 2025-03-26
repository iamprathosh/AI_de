import os

class Config:
    # gRPC settings
    GRPC_SERVER_ADDRESS = os.getenv('GRPC_SERVER_ADDRESS', 'localhost:50051')
    GRPC_MAX_WORKERS = int(os.getenv('GRPC_MAX_WORKERS', 10))

    # IPFS settings
    IPFS_ADDRESS = os.getenv('IPFS_ADDRESS', '/dns/localhost/tcp/5001/http')

    # Serverless settings
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    TRAINING_FUNCTION_NAME = os.getenv('TRAINING_FUNCTION_NAME', 'my_training_function')

    # Security settings
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', 'your_encryption_key')
    JWT_SECRET = os.getenv('JWT_SECRET', 'your_jwt_secret')

    # Fault tolerance settings
    NODE_ADDRESSES = os.getenv('NODE_ADDRESSES', 'localhost:50051,localhost:50052').split(',')

    @staticmethod
    def init_app(app):
        pass
