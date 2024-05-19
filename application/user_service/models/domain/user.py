from typing import Optional

from models.base import BaseSchema, IDSchemaMixin

class UserLogin(BaseSchema):
    email: str
    password: str


class UserBase(BaseSchema):
    first_name: str
    second_name: str
    is_driver: bool

class UserCreate(UserBase, UserLogin):
    pass

class UserSearch(BaseSchema):
    first_name: str
    second_name: str

class UserInDB(UserBase, IDSchemaMixin):
    email: str
    hashed_password: str