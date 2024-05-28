from abc import ABC
from typing import TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.base import Base

from app.models.base import BaseSchema


SQLA_MODEL = TypeVar("SQLA_MODEL", bound=Base)

CREATE_SCHEMA = TypeVar("CREATE_SCHEMA", bound=BaseSchema)
READ_OPTIONAL_SCHEMA = TypeVar("READ_OPTIONAL_SCHEMA", bound=BaseSchema)

class SQLAlchemyRepository(ABC):
    def __init__(
            self,
            db: AsyncSession
        ) -> None:
        self.db = db

    
    sqla_model = SQLA_MODEL

    create_schema = CREATE_SCHEMA
    read_optional_schema = READ_OPTIONAL_SCHEMA

    async def create(
        self, 
        obj_new: create_schema
    ) -> sqla_model | None:
        try:
            db_obj_new = self.sqla_model(**obj_new.dict())
            self.db.add(db_obj_new)

            await self.db.commit()
            await self.db.refresh(db_obj_new)

            return db_obj_new
        
        except Exception as e:

            await self.db.rollback()
            return None
        
    async def read_by_id(
        self, id: int
    ) -> sqla_model | None:
        res = await self.db.get(self.sqla_model, id)

        return res
    

    async def delete(
        self,
        id: int,
    ) -> sqla_model | None:
        res = await self.db.get(self.sqla_model, id)
        if res:
            await self.db.delete(res)
            await self.db.commit()
        else:
            return None
        
        return res