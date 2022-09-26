from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.repository.users_repository import create_new_user, get_user_by_email
from db.db_config import get_db
from schemas.users import UserCreate_schema


router = APIRouter()


@router.post("/")
async def create_user(user: UserCreate_schema, db: Session = Depends(get_db)):
    db_user = await get_user_by_email(email=user.email)
    print(db_user)
    if db_user:
        raise await HTTPException(status_code=status.HTTP_409_CONFLICT,
                                  detail="Email already in use, choose another one")
    user = await create_new_user(user=user, db=db)
    return user
