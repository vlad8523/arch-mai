from pydantic import BaseModel


class UserLogin(BaseModel):
    email: str
    password: str


class UserData(BaseModel):
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
    hashed_password: str
    is_driver: bool
