import os

from app.db.mongo_repositories.base import BaseMongoRepository

class RoutesRepository(BaseMongoRepository):
    collection_name = "ROUTES_COLLECTION"