# CS 340 CRUD Python Module

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username, password):
        """Initialize MongoDB connection using supplied credentials."""

        # Connection Variables
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create a document in the animals collection.
    def create(self, data):
        try:
            if data is not None:
                self.collection.insert_one(data)
                return True
            else:
                return False

        except Exception as e:
            print("Error creating document:", e)
            return False

    # Read document(s) that match the query.
    def read(self, query):
        try:
            if query is not None:
                results = self.collection.find(query)
                return list(results)
            else:
                return []

        except Exception as e:
            print("Error reading documents:", e)
            return []

    # Update document(s) that match the query.
    def update(self, query, new_data):
        try:
            if query is not None and new_data is not None:
                result = self.collection.update_many(
                    query,
                    {"$set": new_data}
                )
                return result.modified_count
            else:
                return 0

        except Exception as e:
            print("Error updating documents:", e)
            return 0

    # Delete document(s) that match the query.
    def delete(self, query):
        try:
            if query is not None:
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                return 0

        except Exception as e:
            print("Error deleting documents:", e)
            return 0