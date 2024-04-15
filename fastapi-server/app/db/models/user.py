# class UserBase(SQLModel):
#     first_name: str
#     second_name: str
#     email: str = Field(unique=True, index=True)
#     login: str


# class UserCreate(UserBase):
#     password: str


# class UserCreateOpen(SQLModel):
#     email: str
#     password: str
#     first_name: str | None = None
#     second_name: str | None = None


# class UserUpdateMe(SQLModel):
#     first_name: str | None = None
#     second_name: str | None = None
#     email: str | None = None


# class UpdatePassword(SQLModel):
#     current_password: str
#     new_password: str


# class User(UserBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     hashed_password: str


# class UserOut(UserBase):
#     id: int


# class UsersOut(SQLModel):
#     data: list[UserOut]
#     count: int


# class UserSearchFirstSecondName(SQLModel):
#     first_name: str
#     second_name: str


# class UserLogin(SQLModel):
#     email: str
#     password: str


from app.db.models.base import Base, BaseDBModel
from app.db.models.metadata import metadata_family

from sqlalchemy import Column, String, Date

class User(Base, BaseDBModel):
    __metadata__ = metadata_family
    
    first_name = Column(String)
    second_name = Column(String)
    email = Column(String)

    