from datetime import datetime
from typing import Optional

from models import Post
from repositories.base import BaseRepository


class PostsRepository(BaseRepository[Post]):
    def __init__(self):
        super(PostsRepository, self).__init__(Post)

    async def create(self, post: Post):
        async with self.session.begin():
            self.session.add(post)
        return None

    async def update(self, id: int, text: Optional[str] = None):
        db_post = (await self.get_all_where(id=id))[0]
        if db_post is not None:
            db_post.text = text
        if db_post in self.session.dirty:  # if updated
            db_post.updated_at = datetime.now()
