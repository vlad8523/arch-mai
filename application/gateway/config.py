import os


class Settings():
    CACHE_EXPIRE_TIME: int = 600
    REDIS_URL: str = f"redis://{os.environ.get('REDIS_URL')}:6379"
    print(f"REDIS_URL {REDIS_URL}")


    USERS_SERVICE_URL: str = f"http://{os.environ.get('USERS_SERVICE_URL')}:8000"
    ROUTES_SERVICE_URL: str = f"http://{os.environ.get('ROUTES_SERVICE_URL')}:8000"
    GATEWAY_TIMEOUT: int = 59


settings = Settings()
