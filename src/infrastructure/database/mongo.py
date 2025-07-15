from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection

class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, name: str) -> Collection:
        return self.db[name]
