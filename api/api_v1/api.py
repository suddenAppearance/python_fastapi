from fastapi import APIRouter

from api.api_v1.endpoints import users, posts, oauth2

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(posts.router, prefix="/posts", tags=["posts"])
router.include_router(oauth2.router, prefix="/oauth2", tags=["oauth2"])