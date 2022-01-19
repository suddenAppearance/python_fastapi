from typing import Optional, List

from pydantic import BaseModel, Field

from models.posts import Post


class BaseUser(BaseModel):
    username: str = Field(min_length=8, regex="[a-zA-Z0-9_]", max_length=16)


class DBUser(BaseUser):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class UserOut(BaseUser):
    id: int

class UserIn(BaseUser):
    pass