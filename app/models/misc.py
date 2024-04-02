from sqlmodel import SQLModel


class Token(SQLModel):
    access_token: str

class Message(SQLModel):
    message: str