from typing import List, Optional
from bson import ObjectId
from domain.models.user import User
from domain.repositories.user_repository import UserRepository
from infrastructure.database.mongo import MongoDB
from infrastructure.schemas.user_schema import user_entity, user_in_db

class UserRepositoryImpl(UserRepository):
    def __init__(self, db: MongoDB):
        self.collection = db.get_collection("users")

    async def get_all_users(self) -> List[User]:
        users = await self.collection.find().to_list(100)
        return [User(**user_entity(user)) for user in users]

    async def create_user(self, user: User) -> User:
        user_dict = user_in_db(user.__dict__)
        result = await self.collection.insert_one(user_dict)
        user.id = str(result.inserted_id)
        return user

    async def find_by_credentials(self, username: str, password: str) -> Optional[User]:
        user = await self.collection.find_one({"username": username, "password": password})
        return User(**user_entity(user)) if user else None

    async def username_exists(self, username: str) -> bool:
        count = await self.collection.count_documents({"username": username})
        return count > 0
