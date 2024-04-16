from typing import Type, Callable, TypeVar

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient

from app.db.mongo_repositories.base import BaseMongoRepository
from app.db.mongodb import db_client

MONGO_REPO_TYPE = TypeVar('MONGO_REPO_TYPE', bound=BaseMongoRepository)


async def get_repository(
    repo_type:  Type[MONGO_REPO_TYPE] 
) -> Callable[[AsyncIOMotorCollection], Type[MONGO_REPO_TYPE]]:
    def get_repo(
        client: AsyncIOMotorClient = db_client
    ) -> Type[AsyncIOMotorCollection]:
        client.get_database(repo_type.db_name).get_collection(repo_type.collection_name)
    
    return get_repo