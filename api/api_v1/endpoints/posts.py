from typing import List

from fastapi import APIRouter

from schemas.posts import PostIn, PostOut, DBPostUpdate
from services.posts import PostsService

router = APIRouter()


@router.post("/")
async def create_post(user_id: int, post: PostIn):
    async with PostsService() as service:
        return await service.create(post, user_id)


@router.get("/", response_model=List[PostOut])
async def list_posts(limit: int = 100, offset: int = 0):
    async with PostsService() as service:
        return await service.get_all(limit, offset)


@router.get("/{id}", response_model=PostOut)
async def get_post(post_id: int):
    async with PostsService() as service:
        return await service.get_by_id(post_id)


@router.patch("/{id}/")
async def partial_update_post(id: int, post: DBPostUpdate):
    async with PostsService() as service:
        return await service.update(id, post)