from pydantic import BaseModel
from sqlalchemy import Column, Date, Float, Integer, String, UniqueConstraint
from sqlalchemy.sql.schema import ForeignKey

from ..db import Base


class Tournament(Base):
    __tablename__ = "tournament"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    manager_id = Column(Integer, ForeignKey("manager.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    game_id = Column(Integer, ForeignKey("game.id"))
    date = Column(Date, nullable=False)
    cost_view = Column(Float, default=0)
    cost_competitor = Column(Float, default=0)
    name = Column("name", String(100), unique=True, nullable=False)
    UniqueConstraint("manager_id", "category_id", name="manager_category"),


class TournamentIn(BaseModel):
    manager_id: int
    category_id: int
    game_id: int
    date: str  # TODO investigar que tipo de dato poner aqui
    cost_view: float
    cost_competitor: float
    name: str


class TournamentOut(BaseModel):
    id: int = 1
    manager_id: int = 123
    category_id: int = 321
    game_id: int = 456
    date: str = "2001-09-28 23:00"  # TODO investigar que tipo de dato poner aqui
    cost_view: float = 0.003
    cost_competitor: float = 0.01
    name: str = "Torneo de League of Legends"
