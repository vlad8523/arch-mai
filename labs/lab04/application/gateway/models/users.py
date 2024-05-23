from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class UserData(BaseModel):
    email: str
    first_name: str
    second_name: str
    is_driver: bool

class UserCreate(UserData, UserLogin):
    pass

class UserSearch(BaseModel):
    first_name: str
    second_name: str


class UserResponse(BaseModel):
    id: int
    first_name: str
    second_name: str
    email: str
    username: str
    hashed_password: str
    is_driver: bool
