import unittest

import numpy as np
import xgboost as xgb

from app.nlp.classifier import predict_sentence


class TestClassifier(unittest.TestCase):
    def setUp(self):
        """Initialize the model and labels before each test."""
        self.model_path = r'/Users/josematos/Dev/Projects/GooseTTS/models/normalization/xgb_model'
        self.model = xgb.Booster()
        self.model.load_model(self.model_path)
        self.labels = np.array(['PLAIN', 'PUNCT', 'DATE', 'LETTERS', 'CARDINAL', 'VERBATIM', 'DECIMAL',
                                'MEASURE', 'MONEY', 'ORDINAL', 'TIME', 'ELECTRONIC', 'DIGIT',
                                'FRACTION', 'TELEPHONE', 'ADDRESS'])

    def test_predict_sentence_plain_text(self):
        """Test prediction for plain text."""
        sentence = "This is a simple sentence."
        tokens, predicted_labels = predict_sentence(sentence, self.model, self.labels)
        self.assertEqual(len(tokens), len(predicted_labels))  # Ensure each token has a prediction

    def test_predict_sentence_with_punctuation(self):
        """Test prediction for text with punctuation."""
        sentence = "Kuklick, p. 75. Kuklick, p. 76. Westcott, p. 124."
        tokens, predicted_labels = predict_sentence(sentence, self.model, self.labels)
        self.assertEqual(len(tokens), len(predicted_labels))  # Ensure each token has a prediction


if __name__ == "__main__":
    unittest.main()
