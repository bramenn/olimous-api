from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .. import db
from ..ticket_v.modelo import TicketViewer


class Viewer(db.Base):
    __tablename__ = "viewer"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column("name", String(100), nullable=False)
    email = Column("email", String(100), nullable=False)
    alias = Column("alias", String(100), nullable=False)
    phone = Column("phone", String(100), nullable=False)
    ticket_v = relationship(TicketViewer)


class ViewerIn(BaseModel):
    name: str
    email: str
    alias: str
    phone: str


class ViewerOut(BaseModel):
    id: int = 1
    name: str = "Briana Delgado"
    email: str = "bridelda@localhost"
    alias: str = "bride"
    phone: str = "51354641341354"
