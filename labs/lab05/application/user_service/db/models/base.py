from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_base, declarative_mixin


Base = declarative_base()


@declarative_mixin
class BaseDBModel:
    id = Column(Integer, primary_key=True, autoincrement=True)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    __mapper_args__ = {"eager_defaults": True}


