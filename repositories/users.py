from sqlalchemy import select

from models.users import User
from repositories.base import async_add, async_execute
from schemas.users import UserIn


class UsersRepository():
    @async_add
    def create(self, user: UserIn):
        return User(
            username=user.username
        )

    @async_execute(one=False)
    def list(self, limit: int, offset: int):
        return select(User).limit(limit).offset(offset)

    @async_execute(one=True)
    def retrieve_by_id(self, user_id: int):
        return select(User).filter(User.id == user_id)

    @async_execute(one=True)
    def retrieve_by_username(self, username: str):
        return select(User).filter(User.username == username)
