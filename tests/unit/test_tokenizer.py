import unittest

from app.nlp.tokenizer import Tokenizer


class TestTokenizer(unittest.TestCase):
    def setUp(self):
        """Initialize the Tokenizer before each test."""
        self.tokenizer = Tokenizer()

    def test_tokenize_plain_text(self):
        """Test tokenization of plain text."""
        sentence = "This is a simple sentence."
        expected_tokens = ['This', 'is', 'a', 'simple', 'sentence', '.']
        tokens = self.tokenizer.tokenize(sentence)
        self.assertEqual(expected_tokens, tokens)

    def test_tokenize_with_punctuation(self):
        """Test tokenization of text with punctuation."""
        sentence = "Kuklick, p. 75. Kuklick, p. 76. Westcott, p. 124."
        expected_tokens = ['Kuklick', ',', 'p', '.', '75', '.', 'Kuklick', ',', 'p', '.', '76', '.', 'Westcott', ',',
                           'p', '.', '124', '.']
        tokens = self.tokenizer.tokenize(sentence)
        self.assertEqual(expected_tokens, tokens)

    def test_tokenize_with_units(self):
        """Test tokenization of text with units."""
        sentence = "(10,200 ft²)"
        expected_tokens = ['(', '10,200 ft', '²', ')']
        tokens = self.tokenizer.tokenize(sentence)
        self.assertEqual(expected_tokens, tokens)

    def test_tokenize_with_dates(self):
        """Test tokenization of text with dates."""
        sentence = "The event is on 2023-10-05."
        expected_tokens = ['The', 'event', 'is', 'on', '2023-10-05', '.']
        tokens = self.tokenizer.tokenize(sentence)
        self.assertEqual(expected_tokens, tokens)

    def test_tokenize_with_money(self):
        """Test tokenization of text with money."""
        sentence = "The price is $10.50."
        expected_tokens = ['The', 'price', 'is', '$10.50', '.']
        tokens = self.tokenizer.tokenize(sentence)
        self.assertEqual(expected_tokens, tokens)


if __name__ == "__main__":
    unittest.main()
