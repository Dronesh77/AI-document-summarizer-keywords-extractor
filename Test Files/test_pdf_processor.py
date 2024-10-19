import unittest
from pdf_processor import PDFProcessor

class TestPDFProcessor(unittest.TestCase):

    def setUp(self):
        # Path to a sample PDF file for testing
        self.pdf_file = "Y:/AI Internship Task Wasserstoff/dataset/pdf1.pdf"  # Change this to a valid PDF path
        self.processor = PDFProcessor()

    def test_extract_text(self):
        """Test the text extraction from a PDF file."""
        text = self.processor.extract_text(self.pdf_file)
        self.assertIsInstance(text, str)  # Check if the output is a string
        self.assertTrue(len(text) > 0)  # Ensure that some text was extracted

    def test_process_pdf(self):
        """Test the processing of a PDF file."""
        result = self.processor.process_pdf(self.pdf_file)
        self.assertIsInstance(result, dict)  # Ensure the result is a dictionary
        self.assertIn("text", result)  # Check if the result contains extracted text
        self.assertIn("metadata", result)  # Check if the result contains metadata
        self.assertTrue(len(result["text"]) > 0)  # Ensure extracted text is not empty

if __name__ == "__main__":
    unittest.main()
