from typing import Optional

from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    username: str = Field(..., min_length=8, regex="[a-zA-Z0-9_]", max_length=16)


class DBUser(BaseUser):
    id: Optional[int] = None
    password_hash: Optional[str] = Field(None, alias="password")
    avatar: Optional[str] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=8, regex="[a-zA-Z0-9_]", max_length=16)


class UserOut(BaseUser):
    id: int
    avatar: Optional[str] = None


class UserIn(BaseUser):
    password: str
    pass
