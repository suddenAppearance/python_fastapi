from models import User
from repositories.users import UsersRepository
from schemas.users import DBUser, DBUserUpdate
from services.base import BaseService


class UsersService(BaseService[User, DBUser]):
    def __init__(self):
        super(UsersService, self).__init__(UsersRepository(), User, DBUser)

    async def get_by_id(self, user_id):
        return await self._get_where(id=user_id)

    async def get_by_username(self, username):
        return await self._get_where(username=username)

    async def create(self, user: DBUser):
        db_user = User(username=user.username)
        return await self.repo.create(db_user)

    async def update(self, id: int, user: DBUserUpdate):
        return await self.repo.update(id, username=user.username)
