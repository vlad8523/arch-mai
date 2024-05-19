from .base import Base, BaseDBModel
from .metadata import metadata_family

from sqlalchemy import Column, String, Boolean  

class User(Base, BaseDBModel):
    __metadata__ = metadata_family
    
    first_name = Column(String)
    second_name = Column(String)
    hashed_password = Column(String)
    email = Column(String)
    is_driver = Column(Boolean)


    