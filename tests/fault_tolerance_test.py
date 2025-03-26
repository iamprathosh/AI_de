import unittest
from unittest.mock import patch, MagicMock
from src.fault_tolerance import FaultToleranceManager

class TestFaultToleranceManager(unittest.TestCase):

    def setUp(self):
        self.nodes = ['localhost:50051', 'localhost:50052']
        self.fault_tolerance_manager = FaultToleranceManager(self.nodes)

    @patch('src.fault_tolerance.grpc.insecure_channel')
    def test_is_node_alive(self, mock_insecure_channel):
        mock_channel = MagicMock()
        mock_insecure_channel.return_value = mock_channel
        mock_channel_ready_future = MagicMock()
        mock_channel_ready_future.result.return_value = True
        with patch('src.fault_tolerance.grpc.channel_ready_future', return_value=mock_channel_ready_future):
            self.assertTrue(self.fault_tolerance_manager.is_node_alive('localhost:50051'))

    @patch('src.fault_tolerance.grpc.insecure_channel')
    def test_is_node_alive_timeout(self, mock_insecure_channel):
        mock_channel = MagicMock()
        mock_insecure_channel.return_value = mock_channel
        mock_channel_ready_future = MagicMock()
        mock_channel_ready_future.result.side_effect = grpc.FutureTimeoutError()
        with patch('src.fault_tolerance.grpc.channel_ready_future', return_value=mock_channel_ready_future):
            self.assertFalse(self.fault_tolerance_manager.is_node_alive('localhost:50051'))

    @patch.object(FaultToleranceManager, 'is_node_alive', return_value=False)
    def test_detect_node_failures(self, mock_is_node_alive):
        self.fault_tolerance_manager.detect_node_failures()
        self.assertIn('localhost:50051', self.fault_tolerance_manager.failed_nodes)

    @patch.object(FaultToleranceManager, 'recover_node')
    def test_recover_from_failures(self, mock_recover_node):
        self.fault_tolerance_manager.failed_nodes = ['localhost:50051']
        self.fault_tolerance_manager.recover_from_failures()
        mock_recover_node.assert_called_once_with('localhost:50051')
        self.assertEqual(self.fault_tolerance_manager.failed_nodes, [])

    @patch('src.fault_tolerance.logging.warning')
    @patch.object(FaultToleranceManager, 'is_node_alive', return_value=False)
    def test_detect_node_failures_logging(self, mock_is_node_alive, mock_logging_warning):
        self.fault_tolerance_manager.detect_node_failures()
        mock_logging_warning.assert_called_once_with('Node localhost:50051 has failed')

    @patch('src.fault_tolerance.logging.error')
    @patch.object(FaultToleranceManager, 'recover_node')
    def test_recover_node_error_handling(self, mock_recover_node, mock_logging_error):
        mock_recover_node.side_effect = Exception('Test error')
        self.fault_tolerance_manager.failed_nodes = ['localhost:50051']
        self.fault_tolerance_manager.recover_from_failures()
        mock_logging_error.assert_called_once_with('Error recovering node localhost:50051: Test error')

if __name__ == '__main__':
    unittest.main()
