import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY = 'e0e5f53b239df3dc39517c34ae0a1c09d1f5d181dfac1578d379a4a5ee3e0ef5'
    ALGORITHM = 'HS256'

    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = 360
    USERS_SERVICE_URL: str = os.environ.get('USERS_SERVICE_URL')
    ORDERS_SERVICE_URL: str = os.environ.get('ORDERS_SERVICE_URL')
    GATEWAY_TIMEOUT: int = 59


settings = Settings()
