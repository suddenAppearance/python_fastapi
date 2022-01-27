from typing import TypeVar, Generic, List, Optional, Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.base import create_async_session, Base

DBModel = TypeVar('DBModel')


class DBException(Exception):
    def __init__(self, message, *errors):
        Exception.__init__(self, message)
        self.errors = errors


class BaseRepository(Generic[DBModel]):
    session: AsyncSession

    def __init__(self, class_: Type[Base]):
        self.class_ = class_
        self.session: AsyncSession = create_async_session()

    async def close(self):
        if self.session is not None:
            try:
                await self.session.commit()
            except Exception as e:
                await self.session.rollback()
                raise DBException(*e.args)
            finally:
                try:
                    await self.session.close()
                except Exception as e:
                    raise DBException(*e.args)

    async def get_all(self, limit: int, offset: int) -> List[DBModel]:
        result = await self.session.execute(select(self.class_).limit(limit).offset(offset))
        return result.scalars().all()

    async def get_all_where(self, **filters) -> List[DBModel]:
        result = await self.session.execute(select(self.class_).filter(
            *[getattr(self.class_, key) == value for key, value in filters.items()]
        ))
        return result.scalars().all()

    async def get_where(self, **filters) -> Optional[DBModel]:
        result = await self.session.execute(select(self.class_).filter(
            *[getattr(self.class_, key) == value for key, value in filters.items()]
        ))
        return result.scalars().one_or_none()
