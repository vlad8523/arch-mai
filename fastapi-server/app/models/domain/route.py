from typing import List
from pydantic import BaseModel




class Route(BaseModel):
    id: str
    start_point: str
    destination_point: str
    driver_ids: int
    passenger_ids: List[int]


class UpdatePassengerList(BaseModel):
    ids: List[int]