from os import access
from typing import Annotated
import aiohttp
from fastapi import APIRouter, Depends, status, HTTPException, Request, Response
from fastapi.security import OAuth2PasswordRequestForm

from auth import generate_access_token, get_current_user, oauth2_scheme
from config import settings
from models.users import UserLogin, UserResponse
from network import make_request

router = APIRouter()

@router.post('/')
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    request: Request, response: Response
):
    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']

    url = f'{settings.USERS_SERVICE_URL}{path}'
    payload = {
        "username": form_data.username,
        "password": form_data.password
    }

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
        return {"access_token": resp_data, "token_type": "bearer"}


@router.get("")
async def get_user(
    current_user: Annotated[dict, Depends(get_current_user)]
):
    return current_user