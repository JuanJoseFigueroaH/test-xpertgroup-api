from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.user import User

class UserRepository(ABC):

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_credentials(self, username: str, password: str) -> Optional[User]:
        pass

    @abstractmethod
    def username_exists(self, username: str) -> bool:
        pass
