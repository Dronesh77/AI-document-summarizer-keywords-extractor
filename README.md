
# Wasserstoff AI Intern Task


## Project Overview
A brief description of what this project does and who it's for

This project implements a dynamic pipeline to process multiple PDF documents, generate domain-specific summaries and keywords, and store the results in a MongoDB database. The pipeline efficiently handles PDFs of varying lengths (short, medium, and long) and uses concurrency to process multiple documents in parallel. Additionally, a Streamlit app is integrated for easy interaction and visualization of the processed results.

**Key Features:**
- Ingests PDFs from a folder and processes them concurrently.
- Generates summaries and extracts domain-specific keywords.
- Stores document metadata, summaries, and keywords in MongoDB.
- Custom error handling for corrupted and unsupported files.
- Scalability for handling large document volumes.
- Interactive Streamlit App to upload and process PDFs with real-time result display.


## System Requirements
To run this project, you will need:

- Python: Version 3.7 or higher
  - Libraries: Install the following Python packages:
    - pymongo==4.3.3
    - spacy==3.5.3
    - requests==2.31.0
    - unittest (comes pre-installed with Python)
    - heapq
    - datetime
    - nltk
    - PyPDF2
    - scikit-learn
    - pytz
    - streamlit (for the web application)


## Installation Steps

1. Clone the repository
```bash
    git clone https://github.com/Dronesh77/dronesh-magare-wasserstoff-AiInternTask.git
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
## Running the Streamlit App
You can now interact with the PDF processor using a Streamlit web interface. To launch the app:

1. Navigate to the project directory and run the Streamlit app:
```bash
streamlit run main.py
```
2. Upload PDFs using the app's file uploader. The pipeline will process the files concurrently, extract summaries, keywords, and other metadata, and display the results in the browser.


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

## PDF Text Extraction (pdf_processor.py)
This module uses the PyPDF2 library to extract raw text from PDF documents. It provides the following method:

- extract_text_from_pdf(pdf_file):
  - Takes the file path of a PDF and extracts text from all its pages.
  - Returns the extracted text as a string.

## Text Processing (text_processor.py)
This module contains text processing functionalities:

- clean_text(text):

  - Cleans the input text by removing stopwords, punctuation, and digits using spaCy's NLP model. It returns the cleaned text as a string.
- summarize_text(text, max_sentences=3):

  - Summarizes the input text by selecting the most relevant sentences based on word frequency. The maximum number of sentences in the summary can be adjusted via the max_sentences parameter.
- extract_keywords_tfidf(corpus, text, max_keywords=10):

  - Extracts keywords from the provided text using the TF-IDF method. It compares the text against a given corpus and returns a list of the most relevant keywords, with the number controlled by the max_keywords parameter.

### Unit Testing
The project includes unit tests to verify the correctness of the text extraction and processing functionalities.

- test_pdf_processor.py:
  - Tests the functionality of the PDF text extraction.
- test_text_processor.py:
  - Tests tokenization, entity recognition, and text preprocessing.


## Example Usage
To use the PDF Text Processor in your own application, you can instantiate the PDFProcessor and TextProcessor classes and call their methods as follows:

``` bash
from pdf_processor import extract_text_from_pdf
from text_processor import summarize_text, extract_keywords_tfidf

# Path to your PDF file
pdf_file = "path_to_your_pdf_file.pdf"

# Extract text from the PDF
text = extract_text_from_pdf(pdf_file)

# Summarize the extracted text
summary = summarize_text(text)

# Extract keywords using a dummy corpus for TF-IDF
corpus = ["some dummy text document", "another document for tfidf"]
keywords = extract_keywords_tfidf(corpus, text)

print(f"Summary: {summary}")
print(f"Keywords: {keywords}")

```
