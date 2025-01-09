from fastapi import APIRouter, HTTPException
from models.db import User
from models.api.user import UserCreate
from database.database import engine, Session

router = APIRouter()

@router.post("/users/")
def create_user(user: UserCreate) -> UserCreate:
    # Создаем сессию для работы с базой данных
    with Session(engine) as session:
        # Проверяем, существует ли уже пользователь с таким email
        existing_user = session.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Создаем нового пользователя
        db_user = User(**user.dict())
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        
        return db_user