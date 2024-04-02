import secrets

import os
from pydantic_settings import BaseSettings
from pydantic import computed_field

from sqlalchemy.engine import URL


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    @computed_field
    @property
    def db_url(self) -> URL:
        return URL.create(
            "postgresql+psycopg2",
            username=os.getenv("DB_LOGIN"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_DATABASE")
        )


settings = Settings()