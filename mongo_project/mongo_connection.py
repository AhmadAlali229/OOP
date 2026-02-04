from pymongo import MongoClient


class MongoDBConnection:
    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.database = None

    def connect(self):
        self.client = MongoClient(self.uri)
        self.database = self.client[self.db_name]
        print("Connected to MongoDB")

    def close(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed")
