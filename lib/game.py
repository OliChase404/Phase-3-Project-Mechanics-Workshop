from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from ipdb import set_trace
from faker import Faker
from rich.console import Console
from rich import print
import random
import time
import os

engine = create_engine("sqlite:///workshop.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
fake = Faker()
console = Console()

terminal_width = os.get_terminal_size().columns
def clear(): return os.system('tput reset')

# Game clock ------------------------------
game_hours = 8
game_days = 1
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def clock(hours):
    global game_hours
    global game_days
    game_hours += hours
    game_days = int(game_hours / 8)
    new_mech_dice_roll()
# ------------------------------


# workshop_funds = 10000


def main_menu():
  day_of_the_week = days[(game_days % 7) - 1]
  current_funds, = session.query(Finance.current_funds).filter_by(id=1).one()
  stats_ticker = f'|--> Day: {game_days} Current funds: ${current_funds} <--|'
  print('🔧' * int(terminal_width / 2))
  console.print("""[bright_red]
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
   [/][bright_yellow]  
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

      [/]""")
  print('🔧' * int(terminal_width / 2))
  print(f'\n{" " * int((terminal_width / 2) - (len(day_of_the_week) / 2))}{day_of_the_week}')
  print(f'\n{" " * int((terminal_width / 2) - (len(stats_ticker) / 2))}{stats_ticker}\n')

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
        clear()
        view_workshop()
  elif choice == '3':
      clock(1)
      clear()
      view_employees()
  elif choice == '4':
      clear()
      view_finances()
  else:
      clear()
      clock(4)
      main_menu()


def view_inbox():
    pass


def view_workshop():
    console.print('''[bright_cyan]
          ||,             |..|: (:)          []     (:)         "   
|||             |..|:   ()                 (:)   xxxxX|
\|''         o  |..|:   (:)        []        ()_   xxX|
 cc88b       Cb |..|:  __||___________________||_   xx|            "
68%8QU89  " d8Ub|..|:_//=========================\  _x| "  cce*88oo       "   "
O0896%68Oo   ||  \.l/=/===========================\|#||  C8O8*8Q8P*Ob o8oo
a%0C88i%8B,,    " /==/=============================\#|/dOB*9*OLS*UOpugO9*D
PQ%OO8OO' |||, "  |..|     __               __ -=  |-' CO*9O0*89PBCOPL*SOBB*
8OUC%CBO%b`|||,,,,|..| O   /\    -=-        /\   O |  " Cgg*bU8*UO*OOd*UOdcb
89Y|//OOP `||||||||..||/| /__\ ___________ /__\ |/||,,,,,,6O*U  /p  gc*U*dpP
  \||       \||||||:.||/|      |##X##X##||      |/||||||||, \\\//  /d*uUP* ,||||||||||||||||||||||||||||||||||||
  |||        `|||||::||/| =-   |XX:XX:XX||      |/||||||||||, \\\////_\ ,,||||||||||||||||||||||||||||||||||||||
:        "         \:||/|      |.::..::.|| =    |/|||||||||||| |||// ,,,||||||||||||||||||||||||||||||||||||||||
::   "     "        \||_|______|........\|______|_||           |||||
:::.      "       "                :  :                "     .//||||\   "           "       "       "       "   
::::::.       "            "     , .           "                     "              "        "  
::%::::::.  "       "    .           :   `              "        "        "       "        "    "
::::::%:::::....              ,   :  . : ` .     "          "
:%:::::::::%::::::::.........:...:.:...:..:...........................::::::::::::::::::::::::::::::::::::::::::
::::::%::::::::::%:::::::::::%:::::::::::::::%:::::::::::::::%::::%::::%::::::::::::::::::::::::::::::::::::::::
`::::::::::%::::::::::::%::::::::::::::%::::::::::::%:::::%::::::::::::::%::::::::::::::::::::::::::::::::::::::

          [/]''')
    print('=' * int(terminal_width))
    all_mechanics = session.query(Mechanic).all()
    all_jobs = session.query(Job).all()
    print('\nCurrent Mechanics:\n')
    for mechanic in all_mechanics:
        print(f'ID: {mechanic.id} - {mechanic.name} - Level: {mechanic.level}')
    print('\nCurrent Jobs:\n')
    for job in all_jobs:
        print(f'Job ID: {job.id} Description: {job.description} - Difficulty: {job.difficulty} Reward: {job.reward}')
    print("""
Commands:
1 = Attempt Repairs
2 = Return to Main Menu
        """)
    # time.sleep(3)

    choice = input('>>> ')
    if choice == '1':
        attempt_repairs()
    elif choice == '2':
        clear()
        main_menu()
    else:
        clear()
        view_workshop()
def attempt_repairs():
    m_id = input('Select a Mechanic to Assign. \nEnter Mechanic ID --> ')
    selected_mechanic = session.query(Mechanic).filter(Mechanic.id == m_id).first()
    print(f"{selected_mechanic.name} has been selected.")
    j_id = input('Select a Job to Assign. \nEnter Job ID --> ')
    selected_job = session.query(Job).filter(Job.id == j_id).first()
    print(f"Job {selected_job.id} has been selected.\n")
    
    if selected_mechanic.level >= selected_job.difficulty:
        chance_of_success = 90
    else: chance_of_success = selected_mechanic.level / selected_job.difficulty * 100
    
    if chance_of_success  > 80:
        print('Chance of success is high')
    elif chance_of_success > 50 and chance_of_success < 80:
        print('Chance of success is medium')
    else: print('Chance of success is low')
    
    cont = input('Execute? (y/n) --> ')
    
    if cont == 'y':
        if chance_of_success > random.randint(0,100):
            console.print('[bright_green]--> Repair Successful!<--[/]')
            dice = random.randint(1,6)
            if dice == 6: 
                console.print(f'[deep_pink1]{selected_mechanic.name} has leveled up![/]')
                session.query(Mechanic).filter(Mechanic.id == m_id).update({Mechanic.level: Mechanic.level + 1})
                session.commit()
            console.print(f'[bright_yellow]${selected_job.reward} Added to Funds![/]')
            session.query(Finance).update({Finance.current_funds: Finance.current_funds + selected_job.reward})
            session.query(Finance).update({Finance.income_this_week: Finance.income_this_week + selected_job.reward})
            session.query(Job).filter(Job.id == j_id).delete()
            session.commit()
            time.sleep(3)
            clear()
            view_workshop()

        else:
            console.print('[bright_red]Repair Failed.[/]')
            owner_compenstation = int(selected_job.reward * random.uniform(0.1, 2))
            print(f'${owner_compenstation} Compensation Paid to Owner for Damage Caused.')
            session.query(Finance).update({Finance.current_funds: Finance.current_funds - owner_compenstation})
            session.query(Job).filter(Job.id == j_id).delete()
            session.commit()
            time.sleep(3)
            clear()
            view_workshop()
    
        


def view_employees():
    employees = session.query(Mechanic).all()
    print('\nCurrent Employees:\n')
    print(employees)
    fire = input('Would you like to fire an employee? (y/n)\n--> ')
    if fire == 'y':
        selcted_employee = input('Enter the ID of the employee to fire --> ')
        if selcted_employee in [str(employee.id) for employee in employees]:
            session.query(Mechanic).filter(
                Mechanic.id == selcted_employee).delete()
            print(f'\n<---Employee Fired--->\n')
            view_employees()
        else:
            clear()
            print(f'\n---Employee {selcted_employee} not found---\n')
            view_employees()
    else:
        clear()
        main_menu()


def view_finances():
    bank = r'''
                                         _._._                       _._._
                                        _|   |_                     _|   |_
                                        | ... |_._._._._._._._._._._| ... |
                                        | ||| |  o NATIONAL BANK o  | ||| |
                                        | """ |  """    """    """  | """ |
                                   ())  |[-|-]| [-|-]  [-|-]  [-|-] |[-|-]|  ())
                                  (())) |     |---------------------|     | (()))
                                 (())())| """ |  """    """    """  | """ |(())())
                                 (()))()|[-|-]|  :::   .-"-.   :::  |[-|-]|(()))()
                                 ()))(()|     | |~|~|  |_|_|  |~|~| |     |()))(()
                                    ||  |_____|_|_|_|__|_|_|__|_|_|_|_____|  ||
                                 ~ ~^^ @@@@@@@@@@@@@@/=======\@@@@@@@@@@@@@@ ^^~ ~
                                      ^~^~                                ~^~^
                                          '''
    current_funds = session.query(Finance.current_funds).filter_by(id=1).one()[0]
    income_this_week, = session.query(Finance.income_this_week).filter_by(id=1).one()
    shop_upkeep, = session.query(Finance.shop_upkeep).filter_by(id=1).one()
    total_salaries, = session.query(Finance.total_salaries).filter_by(id=1).one()
    cap = ('---Capital---')
    c_f =(f'Current Funds: ${current_funds}')
    i_w =(f'Income this week: ${income_this_week}')
    exp = ('---Expenses---')
    s_u =(f'Shop Upkeep: ${shop_upkeep}/Week')
    t_s =(f'Total Salaries: ${total_salaries}')
    t_e =(f'Total Expenses: ${shop_upkeep + total_salaries}')
    print(bank)

    console.print(f"""
{'=' * int(terminal_width)}
\n{" " * int((terminal_width / 2) - (len(cap) / 2))}[bold green]{cap}[/]
\n{" " * int((terminal_width / 2) - (len(c_f) / 2))}{c_f}
\n{" " * int((terminal_width / 2) - (len(i_w) / 2))}{i_w}\n\n
\n{" " * int((terminal_width / 2) - (len(exp) / 2))}[bold red]{exp}[/]
\n{" " * int((terminal_width / 2) - (len(s_u) / 2))}{s_u}
\n{" " * int((terminal_width / 2) - (len(t_s) / 2))}{t_s}
\n{" " * int((terminal_width / 2) - (len(t_e) / 2))}{t_e}\n\n
{'=' * int(terminal_width)}
          """)
    input('Press enter to return to the main menu')
    clear()
    main_menu()
#--------------------------------------------------------------------------------------
    

# Classes/Tables --------------------------------------------------------------------------------------
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
    def __repr__(self):
        return f"'\n'Job ID: {self.id}'\n' Description: {self.description}'\n' Difficulty: {self.difficulty}'\n' Reward: ${self.reward}'\n' Assigned to: {self.assigned_to}'\n'"



class Finance(Base):
    __tablename__ = "finances"

    id = Column(Integer, primary_key=True)
    current_funds = Column(Integer)
    income_this_week = Column(Integer)
    shop_upkeep = Column(Integer)
    total_salaries = Column(Integer)

    # def __repr__(self):
    #   return
def update_finances():
  pass
      
  
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
# --------------------------------------------------------------------------------------




# New Game Setup ------------------------------------------------
m1 = Mechanic(name=fake.name(), level=4, salary=650)
m2 = Mechanic(name=fake.name(), level=2, salary=500)
m3 = Mechanic(name=fake.name(), level=1, salary=350)

j1 = Job(description='Replace clutch pads',
         difficulty=4, reward=1500, assigned_to=m1.id)
j2 = Job(description='Replace starter motor',
         difficulty=2, reward=800, assigned_to=m2.id)
j3 = Job(description='Replace brake pads',
         difficulty=1, reward=500, assigned_to=m3.id)

f1 = Finance(current_funds=10000, income_this_week=0, shop_upkeep=5000, total_salaries=0)

session.add_all([m1, m2, m3, j1, j2, j3, f1])
session.commit()
main_menu()
# ---------------------------------------------------------------