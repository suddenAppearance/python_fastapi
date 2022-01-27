import traceback
from typing import TypeVar, List, Generic, Optional, Type

from fastapi import HTTPException
from sqlalchemy.exc import DBAPIError

from repositories.base import DBException, BaseRepository

DBModel = TypeVar('DBModel')
DataModel = TypeVar('DataModel')


class BaseService(Generic[DBModel, DataModel]):
    def __init__(self, repo, db_model_class, data_model_class):
        self.repo = repo
        self.db_model_class = db_model_class
        self.data_model_class = data_model_class

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self.repo.close()
        except DBException:
            raise HTTPException(status_code=400, detail=f"{str(exc_val)}")

        if exc_type == DBAPIError:
            raise HTTPException(status_code=409, detail=f"{str(exc_val)}")

        elif exc_val is not None:
            raise HTTPException(status_code=500,
                                detail=f"Internal server error. {exc_type}: {exc_val}\n{traceback.format_tb(exc_tb)}")

    def __convert_all(self, instances: List[DBModel]) -> List[DataModel]:
        return [self.__convert(db_user) for db_user in instances]

    def __convert(self, instance: DBModel) -> DataModel:
        return self.data_model_class.from_orm(instance)

    async def get_all(self, limit, offset) -> List[DataModel]:
        db_users: List[DBModel] = await self.repo.get_all(limit, offset)
        return self.__convert_all(db_users)

    async def _get_all_where(self, **filters) -> List[DataModel]:
        db_users: List[DBModel] = await self.repo.get_all_where(**filters)
        return self.__convert_all(db_users)

    async def _get_where(self, **filters) -> Optional[DataModel]:
        db_user: Optional[DBModel] = await self.repo.get_where(**filters)
        return self.__convert(db_user) if db_user is not None else None
