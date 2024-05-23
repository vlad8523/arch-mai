from core.config import get_app_settings
import jwt
from datetime import datetime, timedelta


def generate_access_token(
        data: dict,
        expires_delta: timedelta = timedelta(
            minutes=get_app_settings().ACCESS_TOKEN_EXPIRE_MINUTES
        )
):
    print(data)

    expire = datetime.now() + expires_delta
    token_data = {
        'id': data['id'],
        'username': data['username'],
        'is_driver': data['is_driver'],
        'exp': expire,
    }

    encoded_jwt = jwt.encode(data, get_app_settings().SECRET_KEY, algorithm=get_app_settings().ALGORITHM)
    return encoded_jwt


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
        raise AuthTokenCorrupted('Auth token is corrupted.')