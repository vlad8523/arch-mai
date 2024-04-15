from app.core.config import get_app_settings
from app.db.models.base import Base

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.exc import SQLAlchemyError


async def get_async_engine() -> AsyncEngine:
    try:
        async_engine: AsyncEngine = create_async_engine(
            get_app_settings().database_url,
            future=True
        )
    except SQLAlchemyError as e:
        print("Error on getting Async Engine")
        print(e)

    return async_engine

async def connect():
    async_engine = get_async_engine()
    async with async_engine.begin() as async_conn:

        await async_conn.run_sync(Base.metadata.create_all)
