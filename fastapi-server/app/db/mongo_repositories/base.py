import os

from typing import List
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import get_app_settings

class BaseMongoRepository:
    db_name: str = get_app_settings().mongo_db

    collection_name: str = None

    async def create_collection(self, db_client: AsyncIOMotorClient):
        await db_client.get_database(self.db_name).create_collection(self.collection_name)
        