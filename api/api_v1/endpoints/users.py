from typing import List, Optional

from fastapi import APIRouter

from schemas.users import DBUser, UserOut, UserIn, DBUserUpdate
from services.users import UsersService

router = APIRouter()


@router.get("/", response_model=List[UserOut])
async def list_users(limit: int = 100, offset: int = 0) -> List[DBUser]:
    async with UsersService() as service:
        return await service.get_all(limit, offset)


@router.post("/")
async def create_user(user: UserIn) -> None:
    user = DBUser(**user.dict())
    async with UsersService() as service:
        await service.create(user)


@router.get("/{id}/", response_model=Optional[UserOut])
async def get_user(id: int) -> Optional[DBUser]:
    async with UsersService() as service:
        return await service.get_by_id(id)


@router.patch("/{id}/")
async def partial_update_user(id: int, user: DBUserUpdate):
    async with UsersService() as service:
        return await service.update(id, user)
