# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from ipdb import set_trace

# engine = create_engine("sqlite:///workshop.db")
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()

# class Job(Base):
#     __tablename__ = "jobs"

#     id = Column(Integer, primary_key=True)
#     description = Column(String)
#     difficulty = Column(Integer)
#     reward = Column(Integer)
#     assigned_to = Column(Integer, nullable=True)