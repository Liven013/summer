from sqlmodel import SQLModel


class UserRequest(SQLModel):
    name: str
    surname: str
    email: str
    password: str

class UserLoginRequest(SQLModel):
    email: str
    password: str