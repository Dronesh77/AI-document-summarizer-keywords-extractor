import unittest
from text_processor import TextProcessor

class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        """Set up the TextProcessor instance for testing."""
        self.processor = TextProcessor()
        self.sample_text = "Hello world! This is a test for the Text Processor."

    def test_tokenization(self):
        """Test the tokenization of text."""
        tokens = self.processor.tokenize(self.sample_text)
        self.assertIsInstance(tokens, list)  # Check if the output is a list
        self.assertGreater(len(tokens), 0)  # Ensure that there are tokens extracted

    def test_entity_recognition(self):
        """Test the entity recognition on sample text."""
        entities = self.processor.extract_entities(self.sample_text)
        self.assertIsInstance(entities, list)  # Ensure the output is a list
        # Check if any entities were recognized (adjust based on your text)
        self.assertIn(('Hello', 'GREET'), entities)  # Example entity; adjust according to your implementation

    def test_text_preprocessing(self):
        """Test the text preprocessing method."""
        processed_text = self.processor.preprocess(self.sample_text)
        self.assertIsInstance(processed_text, str)  # Check if the output is a string
        self.assertNotEqual(processed_text, self.sample_text)  # Ensure some preprocessing occurred

if __name__ == "__main__":
    unittest.main()
