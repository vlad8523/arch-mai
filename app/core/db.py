import crud

from sqlalchemy.engine import Engine, create_engine

from collections.abc import Generator

from sqlmodel import Session

from core.config import settings


db_engine: Engine = None


def connect():
    global db_engine

    db_engine = create_engine(url=settings.db_url)

    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(db_engine)

def get_db() -> Generator[Session, None, None]:
    with Session(db_engine) as session:
        yield session