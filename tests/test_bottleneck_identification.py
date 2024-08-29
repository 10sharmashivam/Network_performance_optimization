import unittest
from src.analysis.bottleneck_identification import identify_bottlenecks

class TestBottleneckIdentification(unittest.TestCase):
    def test_identify_bottlenecks(self):
        metrics = {'latency': 120}
        
        # Call identify_bottlenecks and check results
        result = identify_bottlenecks(metrics)
        self.assertEqual(result, 'expected_result')  # Replace with actual expected resultimport unittest
from src.analysis.bottleneck_identification import identify_bottlenecks

class TestBottleneckIdentification(unittest.TestCase):
    
    def test_identify_bottlenecks(self):
        metrics = {'latency': 120}
        result = identify_bottlenecks(metrics)
        self.assertEqual(result, 'High Latency Detected')  # Adjust based on actual expected result

if __name__ == '__main__':
    unittest.main()