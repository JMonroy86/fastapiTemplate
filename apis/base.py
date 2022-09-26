from fastapi import APIRouter
from apis.v1 import route_users
from apis.v1 import route_blogs


api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_blogs.router, prefix="/blogs", tags=["blogs"])
