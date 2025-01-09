from sqlmodel import SQLModel, Field 

class UserCampShiftLink(SQLModel, table = True):
    camp_shift_id : int | None = Field(default = None, foreign_key="campshift.id", primary_key=True)
    user_id : int | None = Field(default = None, foreign_key="user.id", primary_key=True)