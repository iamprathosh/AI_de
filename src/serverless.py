import logging
import boto3
from botocore.exceptions import ClientError

class ServerlessManager:

    def __init__(self, aws_region='us-east-1'):
        self.client = boto3.client('lambda', region_name=aws_region)

    def start_training_task(self, function_name, payload):
        try:
            response = self.client.invoke(
                FunctionName=function_name,
                InvocationType='Event',
                Payload=payload
            )
            logging.info(f"Started training task: {response}")
        except ClientError as e:
            logging.error(f"Error starting training task: {e}")

    def stop_training_task(self, function_name):
        try:
            response = self.client.update_function_configuration(
                FunctionName=function_name,
                Environment={
                    'Variables': {
                        'STOP_TRAINING': 'true'
                    }
                }
            )
            logging.info(f"Stopped training task: {response}")
        except ClientError as e:
            logging.error(f"Error stopping training task: {e}")

    def monitor_training_task(self, function_name):
        try:
            response = self.client.get_function(
                FunctionName=function_name
            )
            logging.info(f"Monitoring training task: {response}")
        except ClientError as e:
            logging.error(f"Error monitoring training task: {e}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    manager = ServerlessManager()
    # Example usage
    manager.start_training_task('my_training_function', '{"key": "value"}')
    manager.monitor_training_task('my_training_function')
    manager.stop_training_task('my_training_function')
