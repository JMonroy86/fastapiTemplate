from fastapi import Request
from core.hashing import Hasher
from schemas.users import UserCreate_schema
# from db.models.users import User
from db.db_config import init_db


async def create_new_user(user: UserCreate_schema, pool):
    hashed_password = Hasher.get_password_hash(user.password)
    async with pool.acquire() as connection:
        async with connection.transaction():
            await connection.execute('''
          INSERT INTO users(username, email, password, is_active, is_superuser) VALUES($1, $2, $3, $4, $5)
      ''', user.username, user.email, hashed_password, user.is_active, user.is_superuser)

            return user


async def get_user_by_email(email):
    db = await init_db()
    print("holasssss", Request.app)
    async with db.acquire() as connection:
        async with connection.transaction():
            return await connection.fetchrow(
                'SELECT * FROM users WHERE email = $1', email)


async def get_user_by_username(username, pool):
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetchrow(
                'SELECT * FROM users WHERE username = $1', username)
