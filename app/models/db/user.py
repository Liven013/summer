from sqlmodel import SQLModel, Relationship, Field
from typing import List, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from .camp_shift import CampShift

class User(SQLModel, table = True):
    id: int = Field(primary_key=True, default=None)
    name: str = Field(nonullable = True)
    surname : str = Field(nonullable = True)
    email : str = Field(unique = True, index = True)
    password_hash : str = Field(nonullable = True)
    bday : date = Field(nonullable = True)

    camp_shifts : List["CampShift"] = Relationship(
        back_populates="users", link_model = "UserCampShiftLink"
    )

