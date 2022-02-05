import binascii
import os
from os import urandom

from fastapi import UploadFile, HTTPException
from passlib.hash import bcrypt

from core import get_settings
from models import User
from repositories.users import UsersRepository
from schemas.users import DBUser, UserUpdate
from services.base import BaseService


class UsersService(BaseService[User, DBUser]):
    def __init__(self):
        super(UsersService, self).__init__(UsersRepository(), User, DBUser)

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hash(password)

    @staticmethod
    def verify_password(password: str, password_hash: str):
        return bcrypt.verify(password, password_hash)

    async def get_by_id(self, user_id):
        return await self._get_where(id=user_id)

    async def get_by_username(self, username):
        return await self._get_where(username=username)

    async def authenticate(self, username: str, password: str):
        user = await self.get_by_username(username)

        if user is None:
            return None

        if self.verify_password(password, user.password_hash):
            return user

        return None

    async def create(self, user: DBUser):
        db_user = User(username=user.username, password_hash=self.hash_password(password=user.password_hash))
        return await self.repo.create(db_user)

    async def update(self, id: int, user: UserUpdate):
        return await self.repo.update(id, username=user.username)

    async def upload_avatar(self, user_id: int, image: UploadFile):
        allowed_extensions = ['.jpg', '.jpeg', '.png']

        extension = None

        for ext in allowed_extensions:
            if image.filename.endswith(ext):
                extension = ext
                break

        if extension is None:
            raise HTTPException(status_code=400, detail="Unsupported image format")

        image.filename = binascii.hexlify(urandom(16)).decode() + extension

        with open(os.path.join(get_settings().MEDIA_ROOT, image.filename), 'wb') as f:
            f.write(await image.read())

        return await self.repo.update(user_id, avatar=image.filename)
