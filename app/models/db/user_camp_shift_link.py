from sqlmodel import SQLModel, Field 

class UserCampShiftLink(SQLModel):
    camp_shift_id : int = Field(foreign_key="campshift.id", primary_key=True)
    user_id : int = Field(foreign_key="user.id", primary_key=True)