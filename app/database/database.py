from sqlmodel import SQLModel, create_engine, Session, sessionmaker
from fastapi import Depends
from models.db import User, CampShift, Organization, UserCampShiftLink

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)
Base = SQLModel

def init_db():
    SQLModel.metadata.create_all(engine)

def get_db(db: Session = Depends(SessionLocal)):
    try:
        yield db
    finally:
        db.close()