from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
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
    
    
def new_mech_dice_roll():
    new_mech_level = random.randint(1, 10)
    new_mech_salary = new_mech_level * 150 + 500
    M1 = Mechanic(name=fake.name(), level=new_mech_level, salary=new_mech_salary)
    dice = random.randint(1, 10)
    if dice > 6:
        query = input(f"""
A new mechanic wants to join your team.
Name: {M1.name}
Level: {M1.level}
Desired salary: {M1.salary}
Do you want to hire him? (y/n) """)
        if query == "y":
            session.add(M1)
            session.commit()
            print(f"{M1.name} has been hired!")
        else:
            print(f"{M1.name} has been rejected.")
        