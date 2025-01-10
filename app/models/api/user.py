from pydantic import BaseModel, EmailStr
from datetime import date

class BaseUser(BaseModel):
    name: str
    surname: str
    email: EmailStr
    bday: date

class UserInDB(BaseUser):
    password_hash: str

    class Config:
        orm_mode = True

class UserIn(BaseUser):
    password: str

class UserOut(BaseUser):
    pass

class UserWithCampShifts(UserOut):
    camp_shifts: list[str]