import sys
import os
# from typing import Any
# from typing import Generator
# from fastapi import FastAPI
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

from unittest.mock import AsyncMock
import pytest

import requests

# from apis.base import api_router


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# this is to include backend dir in sys.path so that we can import from db,main.py


# def start_application():
#     app = FastAPI()
#     app.include_router(api_router)
#     return app


# SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# # Use connect_args parameter only with sqlite
# SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# @pytest.fixture()
# def mock_user(mocker):
#     async_mock = AsyncMock()
#     mocker.patch('db.repository.users_repository.get_user_by_email',
#                  side_effect=async_mock)
#     return async_mock


@pytest.fixture()
def mock_thing(mocker):
    async_mock = AsyncMock()
    mocker.patch('apis.v1.route_users.get_user_by_email',
                 side_effect=async_mock)
    return async_mock


# @pytest.fixture(scope="function")
# def app() -> Generator[FastAPI, Any, None]:
#     """
#     Create a fresh database on each test case.
#     """
#     Base.metadata.create_all(engine)  # Create the tables.
#     _app = start_application()
#     yield _app
#     Base.metadata.drop_all(engine)


# @pytest.fixture(scope="function")
# def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
#     connection = engine.connect()
#     transaction = connection.begin()
#     session = SessionTesting(bind=connection)
#     yield session  # use the session in tests.
#     session.close()
#     transaction.rollback()
#     connection.close()


# @pytest.fixture(scope="function")
# def client(
#     app: FastAPI, db_session: SessionTesting
# ) -> Generator[TestClient, Any, None]:
#     """
#     Create a new FastAPI TestClient that uses the `db_session` fixture to override
#     the `get_db` dependency that is injected into routes.
#     """

#     def _get_test_db():
#         try:
#             yield db_session
#         finally:
#             pass

#     app.dependency_overrides[get_db] = _get_test_db
#     with TestClient(app) as client:
#         yield client
