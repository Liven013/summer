from sqlmodel import SQLModel, Relationship, Field
from typing import TYPE_CHECKING
from datetime import date
from .user_camp_shift_link import UserCampShiftLink

if TYPE_CHECKING:
    from .camp_shift import CampShift
    # from .user_camp_shift_link import UserCampShiftLink

class User(SQLModel, table = True):
    id: int | None = Field(primary_key=True, default=None)
    name: str = Field(nullable = False)
    surname : str = Field(nullable = False)
    email : str = Field(unique = True, nullable = False)
    password_hash : str = Field(nullable = False)
    bday : date = Field(nullable = False)

    camp_shifts : list["CampShift"] = Relationship(
        back_populates="users", link_model = UserCampShiftLink
    )

