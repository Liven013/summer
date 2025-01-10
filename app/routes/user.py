from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from models.api.user import UserIn, UserInDB, UserOut, UserWithCampShifts
from services.user import create_user, update_user, delete_user, get_user_with_camp_shifts
from database.database import get_db

router = APIRouter()

@router.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_new_user(user_in: UserIn, db: Session = Depends(get_db)):
    try:
        user = create_user(user_in, db)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create user")

@router.get("/users/{user_id}", response_model=UserWithCampShifts)
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = get_user_with_camp_shifts(user_id, db)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/users/{user_id}", response_model=UserOut)
def update_existing_user(user_id: int, user_in: UserIn, db: Session = Depends(get_db)):
    try:
        user = update_user(user_id, user_in, db)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to update user")

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    try:
        delete_user(user_id, db)
        return {"message": "User deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to delete user")

@router.get("/users/{user_id}/camp_shifts", response_model=list[str])
def get_user_camp_shifts(user_id: int, db: Session = Depends(get_db)):
    try:
        user = get_user_with_camp_shifts(user_id, db)
        return user.camp_shifts
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))