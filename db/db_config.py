from typing import AsyncGenerator
import databases
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from fastapi import HTTPException

from core.config import Settings

from utils import get_logger

logger = get_logger(__name__)


DATABASE_URL = Settings.DATABASE_URL
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
engine = create_async_engine(
    DATABASE_URL, echo=True,
)

# if you don't want to install postgres or any database, use sqlite, a file system based database,
# uncomment below lines if you would like to use sqlite and comment above 2
# lines of SQLALCHEMY_DATABASE_URL AND engine

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncGenerator:  # new
    async with SessionLocal() as db:
        try:
            yield db
            await db.commit()
        except SQLAlchemyError as sql_ex:
            await db.rollback()
            raise sql_ex
        except HTTPException as http_ex:
            await db.rollback()
            raise http_ex
        finally:
            await db.close()
