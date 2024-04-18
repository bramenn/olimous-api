from pydantic import BaseModel
from sqlalchemy import Column, Date, Float, Integer, String, UniqueConstraint
from sqlalchemy.sql.schema import ForeignKey

from .. import db


class Tournament(db.Base):
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
    date: int  # TODO investigar que tipo de dato poner aqui
    cost_view: float
    cost_competitor: float
    name: str


class TournamentOut(BaseModel):
    id: int
    manager_id: int
    category_id: int
    game_id: int
    date: int  # TODO investigar que tipo de dato poner aqui
    cost_view: float
    cost_competitor: float
    name: str
