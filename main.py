import os
from concurrency_manager import ConcurrencyManager
import logging


# Configure logging
log_file_path = 'Y:/AI_Internship_Task_Wasserstoff/logs/process.log'
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)  # Create directory if it doesn't exist

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(message):
    logging.info(message)
    print(message)  # Print to console as well

def log_error(message):
    logging.error(message)
    print(message)  # Print to console as well


def main():
    # Define paths
    pdf_directory = "Y:/AI_Internship_Task_Wasserstoff/dataset"  # Path to your PDF files
    output_directory = "Y:/AI_Internship_Task_Wasserstoff/output"  # Path to your PDF files

    # Initialize MongoDB handler

    # Initialize Concurrency Manager
    manager = ConcurrencyManager(pdf_directory,output_directory)

    # Process all PDFs
    results = manager.process_all_pdfs()

    # Save results to MongoDB
    for result in results:
        if result is not None:  # Ensure result is valid
            pdf_file = result['filename']
            summary = result['summary']
            keywords = result['keywords']
            summary_id = result['mongodb_id']

            print(f"Pdf File : {pdf_file}\nsummary : {summary}\nkeywords : {keywords}\nID : {summary_id}")

if __name__ == "__main__":
    main()
