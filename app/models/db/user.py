from sqlmodel import SQLModel, Relationship, Field
from typing import List
from datetime import date

class User(SQLModel):
    id: int = Field(primary_key=True, default=None)
    name: str = Field(nonullable = True)
    surname : str = Field(nonullable = True)
    email : str = Field(unique = True, index = True)
    password_hash : str = Field(nonullable = True)
    bday : date = Field(nonullable = True)

    camp_shifts : List["CampShift"] = Relationship(back_populates="user")

