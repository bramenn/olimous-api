from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .. import db
from ..tournament.modelo import Tournament


class Manager(db.Base):
    __tablename__ = "manager"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column("name", String(100), nullable=False)
    email = Column("email", String(50), nullable=False)
    phone = Column("phone", String(15), nullable=False)
    tournament = relationship(Tournament)


class ManagerIn(BaseModel):
    name: str
    email: str
    phone: str


class ManagerOut(BaseModel):
    id: int = 14
    name: str = "Brayan Alejandro Herrera"
    email: str = "brayann.herrera@pragma.com.co"
    phone: str = "57305879123"
