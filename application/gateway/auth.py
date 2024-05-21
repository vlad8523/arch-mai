from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

import jwt

from datetime import datetime, timedelta

from config import settings
from exceptions import AuthTokenMissing, AuthTokenExpired, AuthTokenCorrupted



SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login/")


def generate_access_token(
        data: dict,
        expires_delta: timedelta = timedelta(
            minutes=settings.ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES
        )
):

    expire = datetime.now() + expires_delta
    token_data = {
        'id': data['id'],
        'is_driver': data['is_driver'],
        'exp': expire,
    }

    encoded_jwt = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(authorization: str = None):
    if not authorization:
        raise AuthTokenMissing('Auth token is missing in headers.')

    token = authorization.replace('Bearer ', '')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except jwt.exceptions.ExpiredSignatureError:
        raise AuthTokenExpired('Auth token is expired.')
    except jwt.exceptions.DecodeError:
        raise AuthTokenCorrupted('Auth token is corrupted.')


def generate_request_header(token_payload):
    return {'request-user-id': str(token_payload['id'])}


def is_driver_user(token_payload):
    return token_payload['is_driver']


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = decode_access_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user