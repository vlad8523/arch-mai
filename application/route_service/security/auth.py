from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from core.config import get_app_settings
import jwt

from datetime import datetime, timedelta


SECRET_KEY = get_app_settings().SECRET_KEY
ALGORITHM = get_app_settings().ALGORITHM


def decode_access_token(authorization: str = None):
    if not authorization:
        raise Exception('Auth token is missing in headers.')

    token = authorization.replace('Bearer ', '')
    try:
        payload = jwt.decode(token, get_app_settings().SECRET_KEY, algorithms=get_app_settings().ALGORITHM)
        return payload
    except jwt.exceptions.ExpiredSignatureError:
        raise Exception('Auth token is expired.')
    except jwt.exceptions.DecodeError:
        raise Exception('Auth token is corrupted.')