from typing import List, Optional

from fastapi import APIRouter

from schemas.users import DBUser, UserOut, UserIn
from services.users import UsersService

router = APIRouter()


@router.get("/", response_model=List[UserOut])
async def list_users(limit: int = 100, offset: int = 0) -> List[DBUser]:
    return await UsersService().list(limit, offset)


@router.post("/")
async def create_user(user: UserIn) -> None:
    await UsersService().create(user)


@router.get("/{id}/", response_model=Optional[UserOut])
async def get_user(id: int) -> Optional[DBUser]:
    return await UsersService().retrieve_by_id(id)


