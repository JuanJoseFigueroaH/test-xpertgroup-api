from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    username: str
