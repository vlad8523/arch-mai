from typing import Annotated, Any
import aiohttp

import json

from fastapi import APIRouter, Depends, Request, Response, HTTPException, status
from cache.redis import create_key
from network import make_request

from models.route import CreateRoute, Route
from config import settings
from auth import oauth2_scheme
from cache.redis import r

router = APIRouter()

@router.post("/")
async def create_route(
    route_new: CreateRoute,
    request: Request, response: Response,
    token: Annotated[str, Depends(oauth2_scheme)]
) -> Any:
    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']
    
    url = f'{settings.ROUTES_SERVICE_URL}{path}'

    payload = route_new.model_dump() if route_new else {}

    try: 
        resp_data, status_code = await make_request(
            url=url,
            method=method,
            data=payload,
            headers={"Authentification": f"Bearer {token}"}
        )
    except aiohttp.client_exceptions.ClientConnectorError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Service is unavailable.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    except aiohttp.client_exceptions.ContentTypeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Service error.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    
    response.status_code = status_code
    if status_code == status.HTTP_200_OK:
        return resp_data
    else:
        raise HTTPException(
            status_code=status_code,
            detail=resp_data["detail"]
        )


@router.put("/passenger/{route_id}", response_model=Route)
async def add_passenger(
    route_id: str,
    request: Request, response: Response,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']
    
    url = f'{settings.ROUTES_SERVICE_URL}{path}'

    try: 
        resp_data, status_code = await make_request(
            url=url,
            method=method,
            headers={"Authentification": f"Bearer {token}"}
        )
    except aiohttp.client_exceptions.ClientConnectorError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Service is unavailable.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    except aiohttp.client_exceptions.ContentTypeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Service error.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    
    response.status_code = status_code
    if status_code == status.HTTP_200_OK:
        return resp_data
    else:
        raise HTTPException(
            status_code=status_code,
            detail=resp_data["detail"]
        )


@router.get("/{route_id}", response_model=Route)
async def read_route_by_id(
    route_id: str,
    request: Request, response: Response
) -> Route | None:
    # ,
    # token: Annotated[str, Depends(oauth2_scheme)]
    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']
    
    url = f'{settings.ROUTES_SERVICE_URL}{path}'

    # cache_key = create_key(service=settings.ROUTES_SERVICE_URL,
    #                        method=method,
    #                        path=path,
    #                        token="token")
    
    # cache_route = r.get(cache_key)

    # if cache_route:
    #     print("CACHE DATA")
    #     return json.loads(cache_route)
    
    # print("CACHE IS CLEAR")

    try: 
        resp_data, status_code = await make_request(
            url=url,
            method=method,
            headers={"Authentification": f"Bearer {"token"}"}
        )
    except aiohttp.client_exceptions.ClientConnectorError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Service is unavailable.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    except aiohttp.client_exceptions.ContentTypeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Service error.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    
    # r.set(cache_key, json.dumps(resp_data), ex=settings.CACHE_EXPIRE_TIME)
    
    response.status_code = status_code
    if status_code == status.HTTP_200_OK:
        return resp_data
    else:
        raise HTTPException(
            status_code=status_code,
            detail=resp_data["detail"]
        )


@router.delete("/{route_id}")
async def delete_route_by_id(
    route_id: str,
    request: Request, response: Response,
    token: Annotated[str, Depends(oauth2_scheme)]      
):
    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']
    
    url = f'{settings.ROUTES_SERVICE_URL}{path}'


    try: 
        resp_data, status_code = await make_request(
            url=url,
            method=method,
            headers={"Authentification": f"Bearer {token}"}
        )
    except aiohttp.client_exceptions.ClientConnectorError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Service is unavailable.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    except aiohttp.client_exceptions.ContentTypeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Service error.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    
    response.status_code = status_code
    if status_code == status.HTTP_200_OK:
        return resp_data
    else:
        raise HTTPException(
            status_code=status_code,
            detail=resp_data["detail"]
        )
    