from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient

from route_service.core.config import get_app_settings

from route_service.api.dependencies.mongo_repository import get_repository
from route_service.db.mongo_repositories.routes import RoutesRepository

from route_service.models.domain.route import CreateRoute

db_client = AsyncIOMotorClient(get_app_settings().mongo_uri)

def create_route(route):
    repository = db_client[get_app_settings().mongo_db][RoutesRepository.collection_name]
    loop = db_client.get_io_loop()
    loop.run_until_complete(repository.insert_one(route))
    
create_route(route={
    "start_point": "Moscow",
    "destination_point": "Kazan",
    "driver_id": 1,
    "passenger_ids": [2, 3]
})

create_route(route={
    "start_point": "Kazan",
    "destination_point": "Moscow",
    "driver_id": 1,
    "passenger_ids": [2, 3]
})

create_route(route={
    "start_point": "Saint-Petersburg",
    "destination_point": "Moscow",
    "driver_id": 1,
    "passenger_ids": [4]
})

