from sqlalchemy.orm import Session
from sqlalchemy.future import select
from core.hashing import Hasher
from schemas.users import UserCreate_schema
from db.db_config import SessionLocal
from db.models.users import User


async def create_new_user(user: UserCreate_schema, db: Session):
    user = User(username=user.username,
                email=user.email,
                hashed_password=Hasher.get_password_hash(user.password),
                is_active=True,
                is_superuser=False
                )
    print(user)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user_by_email(email: str):
    print(email)
    async with SessionLocal() as session:
        q = select(User).where(User.email == email)
        result = await session.execute(q)
        curr = result.scalars()
        CACHE = {i.id: i.alias for i in curr}
        return CACHE
