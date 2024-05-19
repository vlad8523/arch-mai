import os


class Settings():
    SECRET_KEY = 'e0e5f53b239df3dc39517c34ae0a1c09d1f5d181dfac1578d379a4a5ee3e0ef5'
    ALGORITHM = 'HS256'

    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = 360
    USERS_SERVICE_URL: str = f"http://{os.environ.get('USERS_SERVICE_URL')}:8000"
    ORDERS_SERVICE_URL: str = f"http://{os.environ.get('ORDERS_SERVICE_URL')}:8000"
    GATEWAY_TIMEOUT: int = 59


settings = Settings()
