
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

## Structure

## Project Structure

```bash
/project_root
    ├── /venv                 # Virtual environment
    ├── /tests                # Unit tests for individual modules
    ├── /data                 # Sample PDFs for testing
    │      ├── sample_short.pdf
    │      ├── sample_medium.pdf
    │      └── sample_long.pdf
    ├── main.py               # Entry point of the pipeline
    ├── pdf_processor.py      # Functions for parsing PDF content
    ├── text_processing.py    # Functions for summarizing and extracting keywords
    ├── mongodb_handler.py    # Functions for interacting with MongoDB
    ├── concurrency_manager.py# Manages parallel processing
    ├── utils.py              # Utility functions (logging, error handling)
    ├── config.py             # Configuration settings (MongoDB, file paths, etc.)
    ├── requirements.txt      # List of dependencies
    └── README.md             # Documentation
