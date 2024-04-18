from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import relationship

from .. import db
from ..tournament.modelo import Tournament


class Category(db.Base):
    __tablename__ = "category"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column("name", String(100))
    alias = Column("alias", String(50))
    description = Column("description", String(300))
    limit_viwers = Column(Integer, default=10)
    limit_participants = Column(Integer, default=5)
    comission = Column(Float, default=0)
    is_free = Column(Boolean, default=True)
    tournament = relationship(Tournament)


class CategoryIn(BaseModel):
    name: str
    alias: str
    description: str
    limit_viwers: int
    limit_participants: int
    comission: float
    is_free: bool


class CategoryOut(BaseModel):
    id: int
    name: str
    alias: str
    description: str
    limit_viwers: int
    limit_participants: int
    comission: float
    is_free: bool
