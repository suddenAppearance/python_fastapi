from fastapi import APIRouter

from api.api_v1.endpoints import users, posts

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(posts.router, prefix="/posts", tags=["posts"])
