from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, UniqueConstraint
from sqlalchemy.sql.schema import ForeignKey

from .. import db


class TicketCompetitor(db.Base):
    __tablename__ = "ticket_c"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    tournament_id = Column(Integer, ForeignKey("tournament.id"))
    competitor_id = Column(Integer, ForeignKey("competitor.id"))
    qr_code = Column("qr_code", String(4000), unique=True, nullable=False)
    is_active = Column(Boolean, default=False)
    was_use = Column(Boolean, default=False)
    UniqueConstraint("tournament_id", "competitor_id", name="tournament_competitor"),


class TicketCompetitorIn(BaseModel):
    tournament_id: int
    competitor_id: int


class TicketCompetitorOut(BaseModel):
    id: int = 1
    tournament_id: int = 123
    competitor_id: int = 321
    qr_code: str = "gckwqvekvgkwecdvkwehvckeuwgvfklwhvfkwqevhfkwjhvfkwqjhvefkjewqvfkewqjhgvcf"
    is_active: bool = False
    was_use: bool = False
    total_price: float = 185.8
    commission: float = 3.1
