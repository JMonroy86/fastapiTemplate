# from typing import Optional
from pydantic import BaseModel, EmailStr


# properties required during user creation
class UserCreate_schema(BaseModel):
    username: str
    email: EmailStr
    password: str
