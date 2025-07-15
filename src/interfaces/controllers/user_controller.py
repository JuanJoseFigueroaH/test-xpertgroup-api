from fastapi import APIRouter, HTTPException, status
from application.dto.user_request import CreateUserRequest, LoginRequest
from application.dto.user_response import UserResponse
from application.use_cases.user_use_case import UserUseCase

router = APIRouter()
use_case: UserUseCase = None

@router.get("/User", response_model=list[UserResponse])
async def get_users():
    return await use_case.get_users()

@router.post("/User", response_model=UserResponse)
async def create_user(data: CreateUserRequest):
    return await use_case.create_user(data)

@router.get("/Login", response_model=UserResponse)
async def login(data: LoginRequest):
    result = await use_case.login(data)
    if not result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return result
