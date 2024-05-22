import os


class Settings():
    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = 360
    USERS_SERVICE_URL: str = f"http://{os.environ.get('USERS_SERVICE_URL')}:8000"
    ROUTES_SERVICE_URL: str = f"http://{os.environ.get('ROUTES_SERVICE_URL')}:8000"
    GATEWAY_TIMEOUT: int = 59


settings = Settings()
