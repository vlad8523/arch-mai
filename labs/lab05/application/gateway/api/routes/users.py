import json
from typing import Annotated
import aiohttp
from fastapi import APIRouter, Depends, status, HTTPException, Request, Response

from cache.redis import create_key, r
from models.users import UserCreate, UserResponse, UserSearch
from config import settings
from network import make_request

from auth import oauth2_scheme


router = APIRouter()


@router.post("/")
async def create_user(
    user_new: UserCreate,
    request: Request, response: Response
) -> UserResponse | None:
    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']
    
    url = f'{settings.USERS_SERVICE_URL}{path}'

    payload = user_new.model_dump() if user_new else {}

    try: 
        resp_data, status_code = await make_request(
            url=url,
            method=method,
            data=payload,
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


@router.get("/{user_id}")
async def get_user(    
    user_id: int,
    request: Request, response: Response,
    token: Annotated[str, Depends(oauth2_scheme)]
) -> UserResponse | None:
    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']
    
    url = f'{settings.USERS_SERVICE_URL}{path}'

    cache_key = create_key(service=settings.ROUTES_SERVICE_URL,
                           method=method,
                           path=path,
                           token=token)

    cache_route = r.get(cache_key)

    if cache_route:
        print("CACHE DATA")
        return json.loads(cache_route)
    
    print("CACHE IS CLEAR")

    try: 
        resp_data, status_code = await make_request(
            url=url,
            method=method,
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
    
    r.set(cache_key, json.dumps(resp_data), ex=settings.CACHE_EXPIRE_TIME)

    response.status_code = status_code
    if status_code == status.HTTP_200_OK:
        return resp_data
    else:
        raise HTTPException(
            status_code=status_code,
            detail=resp_data["detail"]
        )


@router.get("/")
async def get_user_by_name(
    user_search: UserSearch,
    request: Request, response: Response,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']
    
    url = f'{settings.USERS_SERVICE_URL}{path}'

    payload = user_search.model_dump() if user_search else {}

    cache_key = create_key(service=settings.ROUTES_SERVICE_URL,
                           method=method,
                           path=path,
                           token=token)

    cache_route = r.get(cache_key)

    if cache_route:
        print("CACHE DATA")
        return json.loads(cache_route)
    
    print("CACHE IS CLEAR")

    try: 
        resp_data, status_code = await make_request(
            url=url,
            method=method,
            data=payload,
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
    
    r.set(cache_key, json.dumps(resp_data), ex=settings.CACHE_EXPIRE_TIME)

    response.status_code = status_code
    if status_code == status.HTTP_200_OK:
        return resp_data
    else:
        raise HTTPException(
            status_code=status_code,
            detail=resp_data["detail"]
        )


@router.patch("/{user_id}")
async def update_user(
    user_id: int, 
    user_data: UserCreate,
    request: Request, response: Response,
    token: Annotated[str, Depends(oauth2_scheme)]
) -> UserResponse | None:
    auth_token = request.headers.get("Authorization")

    if auth_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No authorization token"
        )

    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']
    
    url = f'{settings.USERS_SERVICE_URL}{path}'

    payload = user_data.model_dump() if user_data else {}

    try: 
        resp_data, status_code = await make_request(
            url=url,
            method=method,
            data=payload,
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
    if status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status_code,
            detail=resp_data["detail"]
        )


    return resp_data
    

@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    request: Request, response: Response,
    token: Annotated[str, Depends(oauth2_scheme)]
) -> UserResponse | None:
    auth_token = request.headers.get("Authorization")

    if auth_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No authorization token"
        )

    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']
    
    url = f'{settings.USERS_SERVICE_URL}{path}'

    try: 
        resp_data, status_code = await make_request(
            url=url,
            method=method,
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
    if status_code != status.HTTP_200_OK:
        raise HTTPException(
            status_code=status_code,
            detail=resp_data["detail"]
        )


    return resp_data
