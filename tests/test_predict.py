
import unittest
from src.predict import predict_staffing_needs

class TestPredict(unittest.TestCase):
    def test_predict(self):
        test_data = [[100, 10, 5]]  # Example input
        predictions = predict_staffing_needs(test_data)
        self.assertIsInstance(predictions, list)

if __name__ == '__main__':
    unittest.main()
