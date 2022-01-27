from typing import Optional

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from core import get_settings
from schemas.users import DBUser
from services.users import UsersService

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/oauth2/token")


async def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends()) -> Optional[DBUser]:
    async with UsersService() as service:
        user: Optional[DBUser] = await service.authenticate(form_data.username, form_data.password)
    return user


@router.post("/token")
async def obtain_token(user: Optional[DBUser] = Depends(authenticate_user)):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    token = jwt.encode(user.dict(), get_settings().SECRET_KEY, algorithm=get_settings().JWT_ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}
