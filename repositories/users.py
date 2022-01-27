from typing import Optional

from models import User
from repositories.base import BaseRepository


class UsersRepository(BaseRepository[User]):
    def __init__(self):
        super(UsersRepository, self).__init__(User)

    async def create(self, user: User) -> None:
        async with self.session.begin():
            self.session.add(user)
        return None

    async def update(self, id: int, username: Optional[str] = None) -> None:
        db_user = (await self.get_all_where(id=id))[0]
        if username is not None:
            db_user.username = username
