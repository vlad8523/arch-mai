from app.models.base import BaseSchema, IDSchemaMixin

class UserLogin(BaseSchema):
    username: str
    password: str


class UserData(BaseSchema):
    email: str
    first_name: str
    second_name: str
    is_driver: bool


class UserCreate(UserData, UserLogin):
    pass


class UserInDB(UserData, IDSchemaMixin):
    email: str
    username: str
    hashed_password: str