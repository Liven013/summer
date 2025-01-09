from sqlmodel import SQLModel, Relationship, Field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .camp_shift import CampShift

class Organization(SQLModel, table = True):
    id : int | None = Field(primary_key=True, default=None)
    name : str = Field(unique=True, nullable=False)
    company : str = Field(nullable = False)

    camp_shifts : list["CampShift"] = Relationship(back_populates= "organization")