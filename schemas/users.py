from typing import Optional

from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    username: str = Field(..., min_length=8, regex="[a-zA-Z0-9_]", max_length=16)


class DBUser(BaseUser):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class DBUserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=8, regex="[a-zA-Z0-9_]", max_length=16)


class UserOut(BaseUser):
    id: int


class UserIn(BaseUser):
    pass
