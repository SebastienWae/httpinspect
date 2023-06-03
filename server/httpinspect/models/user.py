from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, relationship

from httpinspect.database import Base
from httpinspect.models.endpoint import EndpointSchema


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pass


class UserSchema(UserBase):
    id: int
    endpoints: list[EndpointSchema] = []

    class Config:
        orm_mode = True


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)

    endpoints = relationship("Endpoint", back_populates="owner")


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = UserModel(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
