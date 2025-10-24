import unittest
import os
from app import train_model, predict

class TestIrisModel(unittest.TestCase):
    
    def test_train_model(self):
        """Test that model training returns valid accuracy"""
        accuracy = train_model()
        self.assertGreater(accuracy, 0.8)
        self.assertLessEqual(accuracy, 1.0)
        self.assertTrue(os.path.exists('model.pkl'))
    
    def test_predict(self):
        """Test that prediction returns valid class"""
        # Ensure model exists
        if not os.path.exists('model.pkl'):
            train_model()
        
        # Test prediction
        test_features = [5.1, 3.5, 1.4, 0.2]
        result = predict(test_features)
        
        # Result should be between 0 and 2 (three Iris classes)
        self.assertIn(result, [0, 1, 2])
    
    def test_predict_multiple(self):
        """Test predictions for all three classes"""
        if not os.path.exists('model.pkl'):
            train_model()
        
        # Typical features for each class
        test_cases = [
            [5.1, 3.5, 1.4, 0.2],  # Setosa
            [6.5, 3.0, 5.2, 2.0],  # Virginica
            [5.7, 2.8, 4.1, 1.3],  # Versicolor
        ]
        
        for features in test_cases:
            result = predict(features)
            self.assertIn(result, [0, 1, 2])

if __name__ == '__main__':
    unittest.main()

