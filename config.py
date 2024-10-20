import os

# MongoDB Configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")  # Change to your MongoDB URI
DATABASE_NAME = os.getenv("DATABASE_NAME", "PDF_Summary")  # MongoDB database name
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "processed_pdfs")  # MongoDB collection name

# PDF Ingestion Configuration
PDF_FOLDER_PATH = os.path.join(os.path.expanduser("~"), "AI_Internship_Task_Wasserstoff", "dataset")  # Change this path if needed

# Logging Configuration
LOG_FILE_PATH = os.path.join(os.path.expanduser("~"), "AI_Internship_Task_Wasserstoff", "logs", "process.log")  # Path for log files

# Other Configurations
MAX_DOCUMENT_LENGTH = 1000  # Maximum number of words in a summary for long documents
MIN_DOCUMENT_LENGTH = 100  # Minimum number of words for short documents
