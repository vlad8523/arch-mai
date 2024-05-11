from typing import Any

from bson import ObjectId
from fastapi import APIRouter, Depends, status

from starlette.responses import Response
from motor.motor_asyncio import AsyncIOMotorCollection

from app.api.dependencies.mongo_repository import get_repository
from app.db.mongo_repositories.routes import RoutesRepository
from app.db.mongodb import get_filter
from app.models.domain.route import CreateRoute, Route, UpdatePassengerList

router = APIRouter()

@router.post("")
async def create_route(
    route_new: CreateRoute,
    repository: AsyncIOMotorCollection = Depends(get_repository(RoutesRepository))
) -> Any:
    insert_result = await repository.insert_one(dict(route_new))
    return str(insert_result.inserted_id)


@router.put("/passengers/{route_id}", response_model=Route)
async def update_passengers_list(
    route_id: str, 
    passenger_list: UpdatePassengerList,
    repository: AsyncIOMotorCollection = Depends(get_repository(RoutesRepository))
):
    if not ObjectId.is_valid(route_id):
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    
    route = await repository.find_one_and_replace(get_filter(route_id), passenger_list)

    if route is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return route


@router.get("{route_id}", response_model=Route)
async def read_route_by_id(
    route_id: str,
    repository: AsyncIOMotorCollection = Depends(get_repository(RoutesRepository))
):
    if not ObjectId.is_valid(route_id):
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    
    db_route = await repository.find_one(get_filter(route_id))

    if db_route is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return RoutesRepository().map(db_route)


@router.get("{route_id}")
async def delete_route_by_id(
    route_id: str,
    repository: AsyncIOMotorCollection = Depends(get_repository(RoutesRepository))        
):
    if not ObjectId.is_valid(route_id):
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    db_route = await repository.find_one_and_delete(get_filter(route_id))

    if db_route is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return "Succesfully delete route"

