import os
import logging
from datetime import datetime

# Set up logging
def setup_logging(log_file="pipeline.log"):
    """
    Sets up logging configuration.
    :param log_file: Path to the log file.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

# Function to log error messages
def log_error(error_message):
    """
    Logs error messages.
    :param error_message: Error message to log.
    """
    logging.error(error_message)

# Function to log info messages
def log_info(message):
    """
    Logs information messages.
    :param message: Info message to log.
    """
    logging.info(message)

# Check if a file is a PDF
def is_pdf(file_path):
    """
    Checks if a given file is a PDF.
    :param file_path: Path to the file.
    :return: True if the file is a PDF, False otherwise.
    """
    return file_path.lower().endswith('.pdf')

# Create a directory if it doesn't exist
def create_directory(path):
    """
    Creates a directory if it does not already exist.
    :param path: Path to the directory.
    """
    if not os.path.exists(path):
        os.makedirs(path)

# Function to handle errors (example: corrupted PDF)
def handle_error(file_path, error_message):
    """
    Handles errors by logging them and skipping the corrupted files.
    :param file_path: Path of the file where the error occurred.
    :param error_message: Error message.
    """
    log_error(f"Error processing file {file_path}: {error_message}")

# Utility function to get the current timestamp
def get_timestamp():
    """
    Returns the current timestamp as a string.
    :return: Current timestamp.
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Utility function to get file metadata
def get_file_metadata(file):
    """
    Retrieves basic metadata for a file (name, size, path).
    :param file_path: Path to the file.
    :return: Metadata dictionary.
    """
    try:
        file_name = file.name
        file_size = file.size
        return {
            'file_name': file_name,
            'file_size': file_size,
            'processed_time': get_timestamp()
        }
    except Exception as e:
        handle_error(file, str(e))
        return None
