from typing import AsyncGenerator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from db.db import get_async_engine


# DB dependency
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        bind=await get_async_engine(), 
        class_=AsyncSession, 
        autoflush=False,
        expire_on_commit=False,   # document this
    )
    async with async_session() as async_sess:
        try:
            yield async_sess
        except SQLAlchemyError as e:
            pass