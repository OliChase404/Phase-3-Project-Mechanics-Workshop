from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from ipdb import set_trace

engine = create_engine("sqlite:///workshop.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Mechanic(Base):
    __tablename__ = "mechanics"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)
    isHired = Column(Integer)