from db.mongodb import connect as connect_mongo_func


async def startup():
    await connect_mongo_func()
    # await asyncio.gather(connect_postgres, connect_mongo)