from pydantic import BaseModel


class UsernamePasswordForm(BaseModel):
    username: str
    password: str



class LoginResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    first_name: str
    second_name: str
    email: str
    is_driver: bool
    