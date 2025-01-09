from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password_hash: str
    bday: date

    class Config: 
        orm_mode = True