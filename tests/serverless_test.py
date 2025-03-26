import unittest
from unittest.mock import patch, MagicMock
from src.serverless import ServerlessManager

class TestServerlessManager(unittest.TestCase):

    def setUp(self):
        self.serverless_manager = ServerlessManager()

    @patch('boto3.client')
    def test_start_training_task(self, mock_boto_client):
        mock_lambda_client = MagicMock()
        mock_boto_client.return_value = mock_lambda_client
        self.serverless_manager.start_training_task('test_function', '{"key": "value"}')
        mock_lambda_client.invoke.assert_called_once_with(
            FunctionName='test_function',
            InvocationType='Event',
            Payload='{"key": "value"}'
        )

    @patch('boto3.client')
    def test_stop_training_task(self, mock_boto_client):
        mock_lambda_client = MagicMock()
        mock_boto_client.return_value = mock_lambda_client
        self.serverless_manager.stop_training_task('test_function')
        mock_lambda_client.update_function_configuration.assert_called_once_with(
            FunctionName='test_function',
            Environment={
                'Variables': {
                    'STOP_TRAINING': 'true'
                }
            }
        )

    @patch('boto3.client')
    def test_monitor_training_task(self, mock_boto_client):
        mock_lambda_client = MagicMock()
        mock_boto_client.return_value = mock_lambda_client
        self.serverless_manager.monitor_training_task('test_function')
        mock_lambda_client.get_function.assert_called_once_with(
            FunctionName='test_function'
        )

    @patch('boto3.client')
    def test_start_training_task_error_handling(self, mock_boto_client):
        mock_lambda_client = MagicMock()
        mock_lambda_client.invoke.side_effect = Exception('Test error')
        mock_boto_client.return_value = mock_lambda_client
        with self.assertLogs(level='ERROR'):
            self.serverless_manager.start_training_task('test_function', '{"key": "value"}')

    @patch('boto3.client')
    def test_stop_training_task_error_handling(self, mock_boto_client):
        mock_lambda_client = MagicMock()
        mock_lambda_client.update_function_configuration.side_effect = Exception('Test error')
        mock_boto_client.return_value = mock_lambda_client
        with self.assertLogs(level='ERROR'):
            self.serverless_manager.stop_training_task('test_function')

    @patch('boto3.client')
    def test_monitor_training_task_error_handling(self, mock_boto_client):
        mock_lambda_client = MagicMock()
        mock_lambda_client.get_function.side_effect = Exception('Test error')
        mock_boto_client.return_value = mock_lambda_client
        with self.assertLogs(level='ERROR'):
            self.serverless_manager.monitor_training_task('test_function')

if __name__ == '__main__':
    unittest.main()
