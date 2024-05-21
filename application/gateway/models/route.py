from typing import List
from pydantic import BaseModel


class UpdatePassengerList(BaseModel):
    passenger_ids: List[int]


class UpdateDriverId(BaseModel):
    driver_id: int


class CreateRoute(BaseModel):
    start_point: str
    destination_point: str
    driver_id: int
    passenger_ids: List[int] = []


class Route(CreateRoute):
    id: str
    