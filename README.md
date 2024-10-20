
# Wasserstoff AI Intern Task


## Project Overview
A brief description of what this project does and who it's for

This project implements a dynamic pipeline to process multiple PDF documents, generate domain-specific summaries and keywords, and store the results in a MongoDB database. The pipeline efficiently handles PDFs of varying lengths (short, medium, and long) and uses concurrency to process multiple documents in parallel.

**Key Features:**
- Ingests PDFs from a folder and processes them concurrently.
- Generates summaries and extracts domain-specific keywords.
- Stores document metadata, summaries, and keywords in MongoDB.
- Custom error handling for corrupted and unsupported files.
- Scalability for handling large document volumes.


## System Requirements
To run this project, you will need:

- Python: Version 3.7 or higher
- Libraries: Install the following Python packages:
- PyPDF2
- spaCy
- scikit-learn
- numpy
- unittest (comes pre-installed with Python)

## Installation Steps

1. Clone the repository
```bash
    git clone <repository_url>
    cd pdf-text-processor
```

2. Create a Virtual Environment (optional but recommended):
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install Required Packages:
```bash
    pip install PyPDF2 spacy scikit-learn numpy
```

4. Download the spaCy English Language Model:
```bash
    python -m spacy download en_core_web_sm
```
5. Run the Application: You can test the application by executing the test scripts:
```bash
    python test_pdf_processor.py
    python test_text_processor.py
```
## Project Structure

```bash
    /project_root
        ├── /venv                 # Virtual environment
        ├── /Test Files                # Unit tests for individual modules
               ├── test_text_processor.pdf
        │      ├── test_pdf_processor.pdf
        ├── /dataset                 # Sample PDFs for testing
        │      ├── pdf1.pdf
        │      ├── pdf2.pdf
        │      └── ....
        ├── main.py               # Entry point of the pipeline
        ├── pdf_processor.py      # Functions for parsing PDF content
        ├── text_processing.py    # Functions for summarizing and extracting keywords
        ├── mongodb_handler.py    # Functions for interacting with MongoDB
        ├── concurrency_manager.py# Manages parallel processing
        ├── utils.py              # Utility functions (logging, error handling)
        ├── config.py             # Configuration settings (MongoDB, file paths, etc.)
        ├── requirements.txt      # List of dependencies
        └── README.md             # Documentation

```

# Explanation of the silution

## PDFProcessor Class
The PDFProcessor class is responsible for handling PDF files. It has methods for extracting text and metadata from a PDF document. It uses the PyPDF2 library to read PDF files.

### Methods:
- extract_text(pdf_file): Extracts the text from the specified PDF file.
- process_pdf(pdf_file): Processes the PDF file to extract both text and metadata.

### TextProcessor Functions
The text_processor.py module contains functions for cleaning and processing text.

- clean_text(text):

   - Cleans the input text by removing stopwords, punctuation, and digits using spaCy.

- summarize_text(text, max_sentences=3):

  - Summarizes the input text by extracting key sentences based on word frequency. It returns a summary with a maximum number of sentences specified by the user.

- extract_keywords_tfidf(corpus, text, max_keywords=10):

  - Extracts keywords from a given text using the TF-IDF method, leveraging a corpus of documents for context.

### Unit Testing
Unit tests are included in the test_pdf_processor.py and test_text_processor.py files to ensure the correctness of the implemented methods. The tests check for:

- Text extraction functionality
- Text processing and summarization
- Keyword extraction accuracy


## Example Usage
To use the PDF Text Processor in your own application, you can instantiate the PDFProcessor and TextProcessor classes and call their methods as follows:

``` bash
from pdf_processor import PDFProcessor
from text_processor import summarize_text, extract_keywords_tfidf

# Create an instance of PDFProcessor
processor = PDFProcessor()

# Extract text from a PDF file
text = processor.extract_text('path_to_your_pdf_file.pdf')

# Summarize the extracted text
summary = summarize_text(text)

# Extract keywords from the text
keywords = extract_keywords_tfidf(corpus, text)

print(f"Summary: {summary}")
print(f"Keywords: {keywords}")

```
