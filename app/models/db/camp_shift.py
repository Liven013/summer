from sqlmodel import SQLModel, Relationship, Field
from typing import Optional, TYPE_CHECKING
from datetime import date
from .user_camp_shift_link import UserCampShiftLink

if TYPE_CHECKING:
    from .user import User
    from .organization import Organization

class CampShift(SQLModel, table=True):
    id : int | None= Field(primary_key=True, default=None)
    name : str = Field(nullable = False)
    start_date : date = Field(nullable = False)
    end_date : date = Field(nullable = False)
    location : str = Field(nullable = False)

    organization_id : int = Field(default=None, foreign_key='organization.id')
    organization : Optional['Organization'] = Relationship(back_populates='camp_shifts')

    users : list["User"] = Relationship(
        back_populates='camp_shifts', link_model = UserCampShiftLink)


    # tags : Dict() =