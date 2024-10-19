import os
from concurrency_manager import ConcurrencyManager
from mongodb_handler import MongoDBHandler
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
    mongo_db_uri = "mongodb://localhost:27017/"  # Change as necessary
    db_name = "PDF_Summary"  # Your MongoDB database name
    collection_name = "processed_pdfs"  # Your MongoDB collection name

    # Initialize MongoDB handler
    mongo_handler = MongoDBHandler(mongo_db_uri, db_name)

    # Initialize Concurrency Manager
    manager = ConcurrencyManager(pdf_directory,output_directory)

    # Process all PDFs
    results = manager.process_all_pdfs()

    # Save results to MongoDB
    for result in results:
        if result is not None:  # Ensure result is valid
            mongo_handler.insert_summary(result)

    print("All PDFs processed and results saved to MongoDB.")

if __name__ == "__main__":
    main()
