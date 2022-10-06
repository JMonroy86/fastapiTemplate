# from typing import Optional
from pydantic import BaseModel, EmailStr


# properties required during user creation
class UserCreate_schema(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: bool
    is_superuser: bool


class User_schema(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    is_superuser: bool
