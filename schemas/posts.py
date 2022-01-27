from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from schemas.users import UserOut, DBUser


class BasePost(BaseModel):
    text: str


class DBPost(BasePost):
    id: Optional[int] = None
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    user: Optional[DBUser] = None

    class Config:
        orm_mode = True


class DBPostUpdate(BaseModel):
    text: Optional[str] = None


class PostOut(BasePost):
    id: int
    user: UserOut
    created_at: datetime
    updated_at: datetime


class PostIn(BasePost):
    pass
