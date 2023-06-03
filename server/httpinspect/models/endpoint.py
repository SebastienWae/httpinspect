from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String, select
from sqlalchemy.orm import Session, relationship

from httpinspect.database import Base


class EndpointBase(BaseModel):
    name: str


class EndpointCreate(EndpointBase):
    pass


class EndpointSchema(EndpointBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class EndpointModel(Base):
    __tablename__ = "endpoints"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="endpoints")


def get_endpoint(db: Session, endpoint_id: int):
    return db.query(EndpointModel).filter(EndpointModel.id == endpoint_id).first()

def get_enpoints_by_owner_id(db: Session, user_id: int):
    return db.query(EndpointModel).filter(EndpointModel.owner_id == user_id).all()

def search_endpoint_with_name(db: Session, endpoint_name: str):
    db.execute(
        select(
            EndpointModel.
    sometable.c.text.bool_op("@@")(func.to_tsquery("search string")),
),
    )

def get_endpoints(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EndpointModel).offset(skip).limit(limit).all()

def create_endpoint(db: Session )
