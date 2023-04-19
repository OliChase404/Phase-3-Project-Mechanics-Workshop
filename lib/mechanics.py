from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from ipdb import set_trace
from faker import Faker
import random

fake = Faker()

engine = create_engine("sqlite:///workshop.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Mechanic(Base):
    __tablename__ = "mechanics"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)
    salary = Column(Integer)
    isHired = Column(Integer)
    
    
def update_mechanics_table():
    new_mech_level = random.randint(1, 10)
    new_mech_salary = new_mech_level * 150 + 500
    
    M1 = Mechanic(name=fake.name(), level=new_mech_level, salary=new_mech_salary, isHired=0)