from typing import Optional

from app.models.base import BaseSchema, IDSchemaMixin

class UserBase(BaseSchema):
    first_name: str
    second_name: str
    email: str

class UserCreate(UserBase):
    id: int

class UserInDB(UserBase, IDSchemaMixin):
    pass