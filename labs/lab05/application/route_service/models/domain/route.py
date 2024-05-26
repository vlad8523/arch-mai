from typing import List
from pydantic import BaseModel


class CreateRoute(BaseModel):
    start_point: str
    destination_point: str
    driver_id: int = -1
    passenger_list: List[int] = []    


class Route(CreateRoute):
    id: str


class UpdatePassengerList(BaseModel):
    passenger_list: List[int]