from typing import List, Optional
from domain.models.user import User
from domain.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_all_users(self) -> List[User]:
        return self.repository.get_all_users()

    def create_user(self, user: User) -> User:
        base_username = f"{user.first_name.lower()}.{user.last_name.lower()}"
        username = base_username
        i = 1
        while self.repository.username_exists(username):
            username = f"{base_username}{i}"
            i += 1
        user.username = username
        return self.repository.create_user(user)

    def login(self, username: str, password: str) -> Optional[User]:
        return self.repository.find_by_credentials(username, password)
