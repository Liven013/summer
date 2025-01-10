from sqlmodel import Session, select, IntegrityError, selectinload  
from models.db import User
from models.api.user import UserIn, UserInDB, UserWithCampShifts
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_user(user_in: UserIn, db: Session) -> UserInDB:
    stmt = select(User).where(User.email == user_in.email)
    existing_user = db.exec(stmt).first()
    if existing_user:
        raise ValueError("Email already registered")

    user = User(
        name=user_in.name,
        surname=user_in.surname,
        email=user_in.email,
        bday=user_in.bday,
        password_hash=hash_password(user_in.password)
    )
    
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise Exception("Failed to create user")
    
    return user

def get_user_by_id(user_id: int, db: Session) -> UserInDB:
    stmt = select(User).where(User.id == user_id)
    user = db.exec(stmt).first()
    if not user:
        raise ValueError("User not found")
    return user

def update_user(user_id: int, user_in: UserIn, db: Session) -> UserInDB:
    stmt = select(User).where(User.id == user_id)
    user = db.exec(stmt).first()
    if not user:
        raise ValueError("User not found")
    
    user.name = user_in.name
    user.surname = user_in.surname
    user.email = user_in.email
    user.bday = user_in.bday
    user.password_hash = hash_password(user_in.password)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user(user_id: int, db: Session) -> None:
    stmt = select(User).where(User.id == user_id)
    user = db.exec(stmt).first()
    if not user:
        raise ValueError("User not found")
    
    db.delete(user)
    db.commit()

def get_user_with_camp_shifts(user_id: int, db: Session) -> UserWithCampShifts:
    stmt = select(User).where(User.id == user_id).options(selectinload(User.camp_shifts))  # Используем selectinload для подгрузки лагерных смен
    user = db.exec(stmt).first()
    if not user:
        raise ValueError("User not found")

    camp_shifts = [camp_shift.name for camp_shift in user.camp_shifts]
    return UserWithCampShifts(**user.model_dump(), camp_shifts=camp_shifts)