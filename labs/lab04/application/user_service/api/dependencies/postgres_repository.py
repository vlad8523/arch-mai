from typing import Type, TypeVar, Callable

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.base import SQLAlchemyRepository
from api.dependencies.database import get_async_session

SQLA_REPO_TYPE = TypeVar("SQLA_REPO_TYPE", bound=SQLAlchemyRepository)


def get_repository(
    repo_type: Type[SQLA_REPO_TYPE]
) -> Callable[[AsyncSession], Type[SQLA_REPO_TYPE]]:
    def get_repo(
        db: AsyncSession = Depends(get_async_session)
    ) -> Type[SQLA_REPO_TYPE]:
        return repo_type(db=db)
    
    return get_repo