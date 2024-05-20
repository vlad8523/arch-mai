from typing import Optional

from models.base import BaseSchema, IDSchemaMixin

class UserLogin(BaseSchema):
    email: str
    password: str


class UserData(BaseSchema):
    first_name: str
    second_name: str
    is_driver: bool

class UserCreate(UserData, UserLogin):
    pass

class UserSearch(BaseSchema):
    first_name: str
    second_name: str

class UserInDB(UserData, IDSchemaMixin):
    email: str
    hashed_password: str