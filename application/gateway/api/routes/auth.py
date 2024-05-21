import aiohttp
from fastapi import APIRouter, status, HTTPException, Request, Response

from auth import generate_access_token
from config import settings
from models.users import UserLogin
from network import make_request

router = APIRouter()

@router.post('/')
async def login(
    user_form: UserLogin,
    request: Request, response: Response
):
    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']

    url = f'{settings.USERS_SERVICE_URL}{path}'
    payload = user_form.model_dump() if user_form else {}

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
        resp_data = generate_access_token(data=resp_data)

    return resp_data
