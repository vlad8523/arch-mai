from app.db.models.base import Base, BaseDBModel
from app.db.models.metadata import metadata_family

from sqlalchemy import Column, String, Boolean  

class User(Base, BaseDBModel):
    __metadata__ = metadata_family
    
    first_name = Column(String)
    second_name = Column(String)
    username = Column(String)
    hashed_password = Column(String)
    email = Column(String)
    is_driver = Column(Boolean)


    