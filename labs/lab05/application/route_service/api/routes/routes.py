from turtle import mode
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status, Response, Request

from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId

from api.dependencies.mongo_repository import get_repository
from db.mongodb import get_filter
from models.domain.route import CreateRoute, Route
from db.mongo_repositories.routes import RoutesRepository
from security.auth import decode_access_token

from mongo_db_fill import test_data


router = APIRouter()

@router.post("")
async def create_route(
    route_new: CreateRoute,
    request: Request,
    repository: AsyncIOMotorCollection = Depends(get_repository(RoutesRepository))
) -> Any:
    token = request.headers.get("Authentification")

    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token is missed.'
        )

    driver = decode_access_token(token)

    if not driver['is_driver']:
        raise HTTPException(
            status_code=status.HTTP_400_UNAUTHORIZED,
            detail='No rights to create a route.'
        )

    route_new.driver_id = driver["id"]

    print(route_new.driver_id)

    insert_result = await repository.insert_one(route_new.model_dump())

    return str(insert_result.inserted_id)


@router.put("/passenger/{route_id}", response_model=Route)
async def add_passenger(
    route_id: str, 
    request: Request,
    repository: AsyncIOMotorCollection = Depends(get_repository(RoutesRepository))
) -> Route:
    if not ObjectId.is_valid(route_id):
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    token = request.headers.get("Authentification")

    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token is missed.'
        )

    passenger = decode_access_token(token)

    route = await repository.find_one(get_filter(route_id))

    if route is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    del route["_id"]

    route["passenger_list"].append(passenger['id'])

    print(f"DATA BEFORE UPDATE {route}")

    await repository.find_one_and_replace(get_filter(route_id), route)

    print(f"UPDATED ROUTE {route}")
    
    return RoutesRepository().map(await repository.find_one(get_filter(route_id)))


@router.get("/{route_id}", response_model=Route)
async def read_route_by_id(
    route_id: str,
    request: Request,
    repository: AsyncIOMotorCollection = Depends(get_repository(RoutesRepository))
) -> Route | None:
    token = request.headers.get("Authentification")

    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token is missed.'
        )

    if not ObjectId.is_valid(route_id):
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    
    db_route = await repository.find_one(get_filter(route_id))

    if db_route is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
        
    
    print(db_route)

    return RoutesRepository().map(db_route)


@router.delete("/{route_id}")
async def delete_route_by_id(
    route_id: str,
    request: Request,
    repository: AsyncIOMotorCollection = Depends(get_repository(RoutesRepository))        
):
    token = request.headers.get("Authentification")

    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token is missed.'
        )
    
    driver = decode_access_token(token)

    if not driver['is_driver']:
        raise HTTPException(
            status_code=status.HTTP_400_UNAUTHORIZED,
            detail='No rights.'
        )

    if not ObjectId.is_valid(route_id):
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    db_route = await repository.find_one(get_filter(route_id))

    if db_route is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    # if db_route["driver_id"] == driver['id']:
    await repository.find_one_and_delete(get_filter(route_id))
       
    print(f"DELETE ROUTE {db_route}")

    return "Succesfully delete route"


@router.post("/test-data")
async def create_test_data(
    repository: AsyncIOMotorCollection = Depends(get_repository(RoutesRepository))
):
    routes: List[str] = []
    for route_new in test_data:
        try:
            insert_result = await repository.insert_one(route_new.model_dump())
            routes.append(str(insert_result.inserted_id))
        except HTTPException as e:
            raise e

    return routes