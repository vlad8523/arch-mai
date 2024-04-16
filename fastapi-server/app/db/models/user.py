from app.db.models.base import Base, BaseDBModel
from app.db.models.metadata import metadata_family

from sqlalchemy import Column, String, Boolean  

class User(Base, BaseDBModel):
    __metadata__ = metadata_family
    
    first_name = Column(String)
    second_name = Column(String)
    email = Column(String)
    is_driver = Column(Boolean)

    