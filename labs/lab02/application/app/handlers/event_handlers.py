import asyncio

from app.db.db import connect as connect_postgres_func


async def startup():
    await connect_postgres_func()
    # await asyncio.gather(connect_postgres, connect_mongo)