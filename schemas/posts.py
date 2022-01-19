from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from schemas.users import UserOut


class BasePost(BaseModel):
    text: str


class DBPost(BasePost):
    id: Optional[int] = None
    user: Optional[UserOut] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class PostOut(BasePost):
    id: int
    user: UserOut
    created_at: datetime
    updated_at: datetime


class PostIn(BasePost):
    pass
