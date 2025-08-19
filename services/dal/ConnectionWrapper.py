from pymongo import MongoClient
import os

class ConnectionWrapper:

    def __init__(self):

        self.client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017/"))
        self.db = self.client[os.getenv("MONGODB_DATABASE","mydatabase")]


    def get_collection(self, name):
        return self.db[name]



