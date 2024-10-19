import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import config  # Assuming you have the MongoDB connection details in config.py

class MongoDBHandler:
    def __init__(self, mongo_db_uri=config.MONGODB_URI, db_name=config.DATABASE_NAME, collection_name=config.COLLECTION_NAME):
        # Initialize the MongoDB client and database
        self.client = MongoClient(mongo_db_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_summary(self, summary):
        """Insert a new summary into the MongoDB collection."""
        try:
            result = self.collection.insert_one(summary)
            return str(result.inserted_id)  # Return the ID of the inserted document
        except Exception as e:
            print(f"Error inserting summary: {e}")
            return None

    def get_summary(self, summary_id):
        """Retrieve a summary from the MongoDB collection by its ID."""
        try:
            summary = self.collection.find_one({"_id": ObjectId(summary_id)})
            return summary  # Return the found summary
        except Exception as e:
            print(f"Error retrieving summary: {e}")
            return None

    def update_summary(self, summary_id, updated_data):
        """Update a summary in the MongoDB collection."""
        try:
            result = self.collection.update_one({"_id": ObjectId(summary_id)}, {"$set": updated_data})
            return result.modified_count  # Return the count of modified documents
        except Exception as e:
            print(f"Error updating summary: {e}")
            return 0

    def delete_summary(self, summary_id):
        """Delete a summary from the MongoDB collection by its ID."""
        try:
            result = self.collection.delete_one({"_id": ObjectId(summary_id)})
            return result.deleted_count  # Return the count of deleted documents
        except Exception as e:
            print(f"Error deleting summary: {e}")
            return 0

    def close_connection(self):
        """Close the MongoDB connection."""
        self.client.close()

# # Example usage:
# if __name__ == "__main__":
#     db_handler = MongoDBHandler()
    
#     # Example summary to insert
#     summary_data = {
#         "title": "Sample PDF Title",
#         "summary": "This is a summary of the PDF content.",
#         "keywords": ["sample", "pdf", "summary"],
#         "created_at": "2024-10-19"
#     }
    
#     # Insert a summary
#     inserted_id = db_handler.insert_summary(summary_data)
#     print(f"Inserted summary ID: {inserted_id}")
    
#     # Retrieve the summary
#     retrieved_summary = db_handler.get_summary(inserted_id)
#     print("Retrieved summary:", retrieved_summary)

#     # Close the connection
#     db_handler.close_connection()
