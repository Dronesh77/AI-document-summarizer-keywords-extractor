import os

# MongoDB Configuration
MONGODB_URI = "mongodb+srv://dmm12042002:gSgbhH2tNLdk96Sz@cluster0.qm25b.mongodb.net/"        # For MongoDB Atlas

# MONGODB_URI = "mongodb://localhost:27017"        # For MongoDB Compass
DATABASE_NAME = "PDF_Summary"
COLLECTION_NAME = "processed_pdfs"

# MONGODB_URI = os.getenv("MONGODB_URI")  # Mongo DB uri for local host
# DATABASE_NAME = os.getenv("DATABASE_NAME")  # MongoDB database name
# COLLECTION_NAME = os.getenv("COLLECTION_NAME")  # MongoDB collection name

# PDF Ingestion Configuration
PDF_FOLDER_PATH = os.path.join(os.path.expanduser("~"), "AI_Internship_Task_Wasserstoff", "dataset")  # Change this path if needed

# Logging Configuration
LOG_FILE_PATH = os.path.join(os.path.expanduser("~"), "AI_Internship_Task_Wasserstoff", "logs", "process.log")  # Path for log files

# Other Configurations
MAX_DOCUMENT_LENGTH = 1000  # Maximum number of words in a summary for long documents
MIN_DOCUMENT_LENGTH = 100  # Minimum number of words for short documents
