
from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    surname: str
    email: str = Field(unique=True)
    password_hash: str