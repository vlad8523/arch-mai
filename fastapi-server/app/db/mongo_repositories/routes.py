import os

from app.db.mongo_repositories.base import BaseMongoRepository
from motor.motor_asyncio import AsyncIOMotorClient

class RoutesRepository(BaseMongoRepository):
    collection_name = "ROUTES_COLLECTION"