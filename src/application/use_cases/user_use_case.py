from domain.models.user import User
from domain.services.user_service import UserService
from application.dto.user_request import CreateUserRequest, LoginRequest
from application.dto.user_response import UserResponse
from typing import List, Optional

class UserUseCase:
    def __init__(self, service: UserService):
        self.service = service

    async def get_users(self) -> List[UserResponse]:
        users = await self.service.get_all_users()
        return [UserResponse(**u.__dict__) for u in users]

    async def create_user(self, data: CreateUserRequest) -> UserResponse:
        user = User(
            id=None,
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            password=data.password,
            username=""
        )
        created = await self.service.create_user(user)
        return UserResponse(**created.__dict__)

    async def login(self, data: LoginRequest) -> Optional[UserResponse]:
        user = await self.service.login(data.username, data.password)
        return UserResponse(**user.__dict__) if user else None
