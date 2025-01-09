from sqlmodel import SQLModel, Relationship, Field
from typing import List, Optional, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from .user import User
    from .organization import Organization

class CampShift(SQLModel, table=True):
    id : int = Field(primary_key=True, default=None)
    name : str = Field(nonullable = True)
    start_date : date = Field(nonullable = True)
    end_date : date = Field(nonullable = True)

    organization_id : int = Field(default=None, foreign_key='organization.id')
    organization : Optional['Organization'] = Relationship(back_populates='camp_shifts')

    users : List["User"]  = Relationship(
        back_populates='camp_shifts', link_model = "UserCampShiftLink")


    # tags : Dict() =