from typing import List
from pydantic import BaseModel


class CreateRoute(BaseModel):
    start_point: str
    destination_point: str
    


class Route(CreateRoute):
    id: str
    driver_id: int
    passenger_list: List[int]    
    