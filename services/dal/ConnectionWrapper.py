from pymongo import MongoClient
import os

class ConnectionWrapper:

    def __init__(self):
        self.client = MongoClient(
            host=os.getenv("MONGODB_HOST"),
            port=int(os.getenv("MONGODB_PORT", "27017")),
            username=os.getenv("MONGODB_USER"),
            password=os.getenv("MONGODB_PASSWORD"),
            authSource="admin"

        )
        self.db = self.client[os.getenv("MONGODB_DATABASE","mydatabase")]
        self.collection=self.db[os.getenv("MONGO_COLLECTION","soldier_details")]



    def get_collection(self):
        return self.collection



