from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME

def fetch_summaries():
    # Create a MongoDB client
    client = MongoClient(MONGODB_URI)
    
    # Access the specified database
    db = client[DATABASE_NAME]

    # Access the summaries collection (replace 'summaries' with your collection name)
    summaries_collection = db['summaries']

    # Fetch all summaries
    summaries = summaries_collection.find()

    # Print the summaries
    for summary in summaries:
        print(summary)

if __name__ == "__main__":
    fetch_summaries()
