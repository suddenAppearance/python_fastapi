from typing import List, Optional

from models.users import User
from repositories.users import UsersRepository
from schemas.users import UserIn, DBUser
from services.base import Singleton


class UsersService(Singleton):
    repository = UsersRepository()

    async def create(self, user: UserIn) -> None:
        await self.repository.create(user)

    async def list(self, limit: int, offset: int) -> List[DBUser]:
        db_users: List[User] = await self.repository.list(limit, offset)
        return [DBUser.from_orm(db_user) for db_user in db_users]

    async def retrieve_by_id(self, user_id: int) -> Optional[DBUser]:
        user: Optional[User] = await self.repository.retrieve_by_id(user_id)
        if user is None:
            return None
        return DBUser.from_orm(user)

    async def retrieve_by_username(self, username: str) -> Optional[DBUser]:
        user: Optional[User] = await self.repository.retrieve_by_username(username)
        if user is None:
            return None
        return DBUser.from_orm(user)
