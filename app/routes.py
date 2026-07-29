from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from . import crud, schemas, auth

router = APIRouter()


# Register User
@router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.create_user(db, user)

    if new_user is None:
        raise HTTPException(status_code=400, detail="Email already registered")

    return new_user


# Login User (JWT)
@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.login_user(db, user)

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = auth.create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# Get All Users
@router.get("/users", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


# Get User By ID
@router.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# Update User
@router.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id, user)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user


# Delete User
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, user_id)

    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}