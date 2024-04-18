from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .. import db
from ..tournament.modelo import Tournament


class Game(db.Base):
    __tablename__ = "game"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column("name", String(200), nullable=False)
    tournament = relationship(Tournament)


class GameIn(BaseModel):
    name: str


class GameOut(BaseModel):
    id: int
    name: str
