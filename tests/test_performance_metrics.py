import unittest
from unittest.mock import patch, MagicMock
from src.data_collection.performance_metrics import get_snmp_data

class TestPerformanceMetrics(unittest.TestCase):
    @patch('src.data_collection.performance_metrics.snmp_engine')
    def test_get_snmp_data_success(self, mock_snmp):
        # Setup mock
        mock_snmp.return_value = [(1, 'value')]
        
        # Call the function
        result = get_snmp_data('public', '192.168.1.1', 161, '1.3.6.1.2.1.1.1.0')
        
        # Assert the result
        self.assertEqual(result, [(1, 'value')])

    @patch('src.data_collection.performance_metrics.snmp_engine')
    def test_get_snmp_data_timeout(self, mock_snmp):
        # Setup mock to raise a timeout
        mock_snmp.side_effect = RequestTimedOut()
        
        # Call the function
        result = get_snmp_data('public', '192.168.1.1', 161, '1.3.6.1.2.1.1.1.0')
        
        # Assert the result
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()