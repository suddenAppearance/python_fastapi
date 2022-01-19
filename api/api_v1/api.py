from fastapi import APIRouter

from api.api_v1.endpoints import users

router = APIRouter()

router.include_router(users.router, prefix="/users")
