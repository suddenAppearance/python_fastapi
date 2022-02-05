from typing import List, Optional

from fastapi import APIRouter, Depends, UploadFile, File

from api.api_v1.deps import get_current_user
from schemas.users import DBUser, UserOut, UserIn, UserUpdate
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


@router.get("/me/", response_model=UserOut)
async def get_current_user(user: DBUser = Depends(get_current_user)):
    return user


@router.get("/{id}/", response_model=UserOut)
async def get_user(id: int) -> Optional[DBUser]:
    async with UsersService() as service:
        return await service.get_by_id(id)


@router.patch("/{id}/")
async def partial_update_user(id: int, user: UserUpdate):
    async with UsersService() as service:
        return await service.update(id, user)


@router.post("/{id}/uploadAvatar/", include_in_schema=False)  # use include_in_schema=False, because it breaks Swagger
async def upload_avatar(id: int, file: UploadFile = File(...)):
    async with UsersService() as service:
        return await service.upload_avatar(id, file)
