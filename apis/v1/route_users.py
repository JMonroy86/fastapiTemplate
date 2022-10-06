from fastapi import APIRouter, Request
from fastapi import HTTPException, status
from db.repository.users_repository import create_new_user
from db.repository.users_repository import get_user_by_email
from db.repository.users_repository import get_user_by_username
from schemas.users import UserCreate_schema


router = APIRouter()


@router.post("/")
async def create_user(user: UserCreate_schema, request: Request):
    email_exist = await get_user_by_email(email=user.email)
    username_exist = await get_user_by_username(username=user.username, pool=request.app.state.pool)
    if email_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Email already in use, choose another one")
    if username_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Username already in use, choose another one")

    user = await create_new_user(user=user, pool=request.app.state.pool)

    return user


@router.get("/{email}")
async def get_user(email: str):
    user = await get_user_by_email(email)
    print(email)
    if user:
        return {
            "username": user["username"],
            "email": user["email"],
            "is_active": user["is_active"],
            "is_superuser": user["is_superuser"],
        }

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Email not found")
