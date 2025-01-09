from sqlmodel import SQLModel, Relationship, Field
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .camp_shift import CampShift

class Organization(SQLModel, table = True):
    id : int = Field(primary_key=True, default=None)
    name : str = Field(unique=True, nonullable=True)
    company : str = Field(nonullable = True)

    camp_shifts : List["CampShift"] = Relationship(back_populates= "organization")