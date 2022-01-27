from datetime import datetime
from typing import Optional

from models import Post
from repositories.posts import PostsRepository
from schemas.posts import DBPost
from schemas.users import DBUser
from services.base import BaseService


class PostsService(BaseService[Post, DBPost]):
    def __init__(self):
        super(PostsService, self).__init__(PostsRepository(), Post, DBPost)

    async def get_by_id(self, post_id) -> Optional[DBPost]:
        return await self._get_where(id=post_id)

    async def get_by_user(self, user: DBUser):
        return await self._get_all_where(user_id=user.id)

    async def create(self, post: DBPost, user_id: int):
        db_post = Post(
            text=post.text,
            user_id=user_id,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        await self.repo.create(db_post)

    async def update(self, id: int, post: DBPost):
        return await self.repo.update(id, text=post.text)
