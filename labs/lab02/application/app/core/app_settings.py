import secrets

import os
from pydantic import computed_field

from sqlalchemy.engine import URL


class AppSettings():
    postgres_driver: str = "asyncpg"
    postgres_user: str = os.getenv("DB_LOGIN")
    postgres_password = os.getenv("DB_PASSWORD")
    postgres_host = os.getenv("DB_HOST")
    postgres_port = os.getenv("DB_PORT")
    postgres_db = os.getenv("DB_DATABASE")

    @property
    def database_url(self) -> URL:
        return URL.create(
            f"postgresql+{self.postgres_driver}",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db
        )