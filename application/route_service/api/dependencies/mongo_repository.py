from typing import Type, Callable, TypeVar

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient

from db.mongo_repositories.base import BaseMongoRepository, get_client

MONGO_REPO_TYPE = TypeVar('MONGO_REPO_TYPE', bound=BaseMongoRepository)


def get_repository(
    repo_type:  Type[MONGO_REPO_TYPE]
) -> Callable[[AsyncIOMotorCollection], Type[MONGO_REPO_TYPE]]:
    def get_repo(db_client: AsyncIOMotorClient = Depends(get_client)) -> AsyncIOMotorCollection: 
         
        if db_client is None: 
            print("db_client is none")
        return db_client.get_database(repo_type.db_name).get_collection(repo_type.collection_name)

    return get_repo    
