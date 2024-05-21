import os
from typing import Any

from db.mongo_repositories.base import BaseMongoRepository
from models.domain.route import Route


class RoutesRepository(BaseMongoRepository):
    collection_name = "ROUTES_COLLECTION"

    def map(self, route: Any) -> Route:       
        return Route(
            id=str(route['_id']),
            start_point=route['start_point'],
            destination_point=route['destination_point'],
            driver_id=route['driver_id'],
            passenger_ids=route['passenger_ids']
        )