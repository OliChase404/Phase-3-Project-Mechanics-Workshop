from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ipdb import set_trace
from faker import Faker
from clock import clock
import random
import os

engine = create_engine("sqlite:///workshop.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

fake = Faker()

game_hours = 8
game_days = int(game_hours / 8)


def clock(hours):
    global game_hours
    game_hours += hours
    new_mech_dice_roll()


workshop_funds = 10000
stats_ticker = f'|--> Day: {game_days} Current funds: ${workshop_funds} <--|'

terminal_width = os.get_terminal_size().columns
def clear(): return os.system('tput reset')


def main_menu():
    clock(1)
    print('🔧' * int(terminal_width / 2))
    print("""
            ___           ___                       ___           ___           ___           ___           ___   
     /  /\         /__/\          ___        /  /\         /  /\         /__/\         /  /\         /  /\  
    /  /::\        \  \:\        /  /\      /  /::\       /  /:/_        \  \:\       /  /::\       /  /::\ 
   /  /:/\:\        \  \:\      /  /:/     /  /:/\:\     /  /:/ /\        \__\:\     /  /:/\:\     /  /:/\:
  /  /:/~/::\   ___  \  \:\    /  /:/     /  /:/  \:\   /  /:/ /::\   ___ /  /::\   /  /:/  \:\   /  /:/~/:/
 /__/:/ /:/\:\ /__/\  \__\:\  /  /::\    /__/:/ \__\:\ /__/:/ /:/\:\ /__/\  /:/\:\ /__/:/ \__\:\ /__/:/ /:/ 
 \  \:\/:/__\/ \  \:\ /  /:/ /__/:/\:\   \  \:\ /  /:/ \  \:\/:/~/:/ \  \:\/:/__\/ \  \:\ /  /:/ \  \:\/:/  
  \  \::/       \  \:\  /:/  \__\/  \:\   \  \:\  /:/   \  \::/ /:/   \  \::/       \  \:\  /:/   \  \::/   
   \  \:\        \  \:\/:/        \  \:\   \  \:\/:/     \__\/ /:/     \  \:\        \  \:\/:/     \  \:\   
    \  \:\        \  \::/          \__\/    \  \::/        /__/:/       \  \:\        \  \::/       \  \:\  
     \__\/         \__\/                     \__\/         \__\/         \__\/         \__\/         \__\/  
                                       ___           ___           ___           ___                        
               ___         ___        /  /\         /  /\         /  /\         /__/\                       
              /  /\       /__/|      /  /:/        /  /::\       /  /::\        \  \:\                      
             /  /:/      |  |:|     /  /:/        /  /:/\:\     /  /:/\:\        \  \:\                     
            /  /:/       |  |:|    /  /:/  ___   /  /:/  \:\   /  /:/  \:\   _____\__\:\                    
           /  /::\     __|__|:|   /__/:/  /  /\ /__/:/ \__\:\ /__/:/ \__\:\ /__/::::::::\                   
          /__/:/\:\   /__/::::\   \  \:\ /  /:/ \  \:\ /  /:/ \  \:\ /  /:/ \  \:\~~\~~\/                   
          \__\/  \:\      \~~\:\   \  \:\  /:/   \  \:\  /:/   \  \:\  /:/   \  \:\                      
               \  \:\      \  \:\   \  \:\/:/     \  \:\/:/     \  \:\/:/     \  \:\                        
                \__\/       \__\/    \  \::/       \  \::/       \  \::/       \  \:\                       
                                      \__\/         \__\/         \__\/         \__\/  

      """)
    print('🔧' * int(terminal_width / 2))
    print(
        f'\n{" " * int((terminal_width / 2) - (len(stats_ticker) / 2))}{stats_ticker}\n')

    print("""
Commands:
  1 = View Inbox
  2 = View Workshop
  3 = View Employees
  4 = View Finances
          """)

    choice = input('>>> ')
    if choice == '1':
        view_inbox()
    elif choice == '2':
        pass
    elif choice == '3':
        clock(1)
        clear()
        view_employees()


def view_inbox():
    clock(1)
    clear()
    main_menu()


def view_workshop():
    pass


def view_employees():
    employees = session.query(Mechanic).all()
    print(employees)
    fire = input('Would you like to fire an employee? (y/n)')
    if fire == 'y':
        selcted_employee = input('Enter the ID of the employee to fire --> ')
        if selcted_employee in [str(employee.id) for employee in employees]:
            session.query(Mechanic).filter(
                Mechanic.id == selcted_employee).delete()
            view_employees()
        else:
            clear()
            print(f'\n---Employee {selcted_employee} not found---\n')
            view_employees()
    else:
        clear()
        main_menu()


def view_finances():
    pass

# --------------------------------------------------------------------------------------


class Mechanic(Base):
    __tablename__ = "mechanics"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)
    salary = Column(Integer)

    def __repr__(self):
        return f"'\n'Employee ID: {self.id}'\n' Name: {self.name}'\n' Level: {self.level}'\n' Salary: ${self.salary} '\n'"


def new_mech_dice_roll():
    new_mech_level = random.randint(1, 10)
    new_mech_salary = new_mech_level * 150 + 500
    M1 = Mechanic(name=fake.name(), level=new_mech_level,
                  salary=new_mech_salary)
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


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    difficulty = Column(Integer)
    reward = Column(Integer)
    assigned_to = Column(Integer, nullable=True)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
# --------------------------------------------------------------------------------------


m1 = Mechanic(name=fake.name(), level=4, salary=650)
m2 = Mechanic(name=fake.name(), level=2, salary=500)
m3 = Mechanic(name=fake.name(), level=1, salary=350)

j1 = Job(description='Replace clutch pads',
         difficulty=4, reward=1500, assigned_to=m1.id)
j2 = Job(description='Replace starter motor',
         difficulty=2, reward=800, assigned_to=m2.id)
j3 = Job(description='Replace brake pads',
         difficulty=1, reward=500, assigned_to=m3.id)

session.add_all([m1, m2, m3, j1, j2, j3])
session.commit()

# set_trace()


main_menu()
