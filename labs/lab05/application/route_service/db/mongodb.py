from core.config import get_app_settings
from bson import ObjectId

from motor.motor_asyncio import AsyncIOMotorClient

db_client: AsyncIOMotorClient = None

async def get_client() -> AsyncIOMotorClient | None:
    global db_client
    
    if db_client is None:
        db_client = AsyncIOMotorClient(get_app_settings().mongo_uri)
    
    return db_client


async def connect():
    try:
        db_client = await get_client()
        await db_client.server_info()

        print(f"Connected to mongo with uri {get_app_settings().mongo_uri}")

        # if get_app_settings().mongo_db not in await db_client.list_database_names():
        #     print(f"list of databases {await db_client.list_database_names()}")
        #     await RoutesRepository().create_collection(db_client)

    except Exception as e:
        print(e)
        print(f"Can't connect to mongo {get_app_settings().mongo_uri}")

def get_filter(_id: str) -> dict:
    return {'_id': ObjectId(_id)}
    