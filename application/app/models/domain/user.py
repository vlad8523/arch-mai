from typing import Optional

from app.models.base import BaseSchema, IDSchemaMixin

class UserBase(BaseSchema):
    first_name: str
    second_name: str
    email: str
    is_driver: bool

class UserCreate(UserBase):
    id: int

class UserSearch(BaseSchema):
    first_name: str
    second_name: str

class UserInDB(UserBase, IDSchemaMixin):
    pass