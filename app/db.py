from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import POSTGRES_URI

conn = create_engine(POSTGRES_URI, pool_pre_ping=True, pool_recycle=150)

Session = sessionmaker(bind=conn)

session = Session()
Base = declarative_base()
