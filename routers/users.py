import sys
sys.path.append("..")

from fastapi import Depends, APIRouter
from pydantic import BaseModel
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from .auth import get_current_user, get_user_exception, verify_password, get_password_hash

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str

@router.get("/all")
def read_all_user(db: Session = Depends(get_db)):
    return db.query(models.Users).all()

@router.get("/user/{user_id}")
def read_user_path(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id == user_id).first()
    if user_model is not None:
        return user_model
    return get_user_exception()

@router.get("/user/")
def read_user_query(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id == user_id).first()
    if user_model is not None:
        return user_model
    return get_user_exception()

@router.put("/user/password")
def update_password(user_verification: UserVerification,
                    user: dict = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    if user_model is not None:
        if user_verification.username == user_model.username and verify_password(
                user_verification.password,
                user_model.hashed_password):
            user_model.hashed_password = get_password_hash(user_verification.new_password)
            db.add(user_model)
            db.commit()
            return "successful"
    return get_user_exception()

@router.delete("/user")
def delete_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    if user is None:
        return get_user_exception()

    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    if user_model is None:
        return get_user_exception()

    db.query(models.Users).filter(models.Users.id == user.get("id")).delete()
    db.commit()

    return "Delete successful"