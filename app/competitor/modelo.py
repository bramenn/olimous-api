from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .. import db
from ..ticket_c.modelo import TicketCompetitor


class Competitor(db.Base):
    __tablename__ = "competitor"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column("name", String(100), nullable=False)
    email = Column("email", String(100), nullable=False)
    alias = Column("alias", String(100), nullable=False)
    phone = Column("phone", String(100), nullable=False)
    ticket_c = relationship(TicketCompetitor)


class CompetitorIn(BaseModel):
    name: str
    email: str
    alias: str
    phone: str


class CompetitorOut(BaseModel):
    id: int = 1
    name: str = "Sebastian Durango"
    email: str = "sebasdurango@localhost"
    alias: str = "sebis"
    phone: str = "573123456789"
