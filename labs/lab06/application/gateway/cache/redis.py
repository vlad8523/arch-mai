import redis

from config import settings

r = redis.from_url(url=settings.REDIS_URL)


def create_key(service: str,
               method: str, 
               path: str,
               token: str):
    return f"{service} {method} {path} {token}"