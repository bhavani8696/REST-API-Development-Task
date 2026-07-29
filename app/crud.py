from sqlalchemy.orm import Session
from . import models, auth
from .schemas import UserCreate, UserUpdate, UserLogin


# Register User
def create_user(db: Session, user: UserCreate):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        return None

    db_user = models.User(
        name=user.name,
        email=user.email,
        password=auth.hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# Login User
def login_user(db: Session, user: UserLogin):
    db_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if db_user is None:
        return None

    if not auth.verify_password(user.password, db_user.password):
        return None

    return db_user


# Get All Users
def get_users(db: Session):
    return db.query(models.User).all()


# Get User By ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()


# Update User
def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if db_user is None:
        return None

    db_user.name = user.name
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)

    return db_user


# Delete User
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if db_user is None:
        return None

    db.delete(db_user)
    db.commit()

    return db_user