import unittest
from src.analysis.traffic_analysis import analyze_traffic

class TestTrafficAnalysis(unittest.TestCase):
    def test_analyze_traffic(self):
        # Example packet data
        packets = [{'layer': 'TCP'}, {'layer': 'UDP'}]  # Update with actual expected packet structure
        
        # Call the function
        result = analyze_traffic(packets)
        
        # Assert the result
        self.assertTrue(result)  # Adjust based on actual expected result

if __name__ == '__main__':
    unittest.main()