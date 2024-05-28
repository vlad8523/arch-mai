from db.db import connect


async def startup():
    await connect()