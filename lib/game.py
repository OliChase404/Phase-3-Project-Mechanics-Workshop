from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from functions import random_job
from rich.console import Console
from ipdb import set_trace
from faker import Faker
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
current_day = 'Monday'
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def clock(hours):
    global game_hours
    global game_days
    game_hours += hours
    game_days = int(game_hours / 8)
    # new_mech_dice_roll()
# ------------------------------



# Main Menu --------------------------------
def main_menu():
    clock(1)
    check_day()
    day_of_the_week = days[(game_days % 7) - 1]
    current_funds, = session.query(Finance.current_funds).filter_by(id=1).one()
    stats_ticker = f'|--> Day: {game_days} Current funds: ${current_funds} <--|'
    
    print('🔧' * int(terminal_width / 2))
    console.print("""[bright_cyan]
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
   [/][bright_red]  
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
1 = View Computer
2 = Visit Workshop
3 = Visit Bank
        """)
    
    choice = input('>>> ')
    if choice == '1':
        clear()
        view_computer()
    elif choice == '2':
          clear()
          view_workshop()
    elif choice == '3':
        clear()
        view_finances()
    else:
        clear()
        main_menu()
#-----------------------------------------



#--------------COMPUTER FUNCTIONS----------------#
def view_computer():
    clock(1)
    print('=' * int(terminal_width))
    console.print('''[bright_blue]
                                 .,,uod8B8bou,,.
                        ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
                   ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
                   !...:!TVBBBRPFT||||||||||!!^^""'   ||||
                   !.......:!?|||||!!^^""'            ||||
                   !.........||||                     ||||
                   !.........||||                     ||||
                   !.........||||                     ||||
                   !.........||||                     ||||
                   !.........||||                     ||||
                   !.........||||                     ||||
                   `.........||||                    ,||||
                    .;.......||||               _.-!!|||||
             .,uodWBBBBb.....||||       _.-!!|||||||||!:'
          !YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
          !..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
          !....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
          !......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
          !........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
          `..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
            `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
              `........::::::::::::::::;iof688888888888888888888b.     `
                `......:::::::::;iof688888888888888888888888888888b.
                  `....:::;iof688888888888888888888888888888888899fT!
                    `..::!8888888888888888888888888888888899fT|!^"'
                      `' !!988888888888888888888888899fT|!^"'
                          `!!8888888888888888899fT|!^"'
                            `!988888888899fT|!^"'
                              `!9899fT|!^"'
                                `!^"'
                  [/]''')
    print('=' * int(terminal_width))
    print("""
Commands:
1 = View Available Jobs
2 = View Mechanic Resumes
3 = Review Employees
4 = Return to Main Menu
        """)
    choice = input('>>> ')
    if choice == '1':
        view_available_jobs()
    elif choice == '2':
        view_resumes()
    elif choice == '3':
        clear()
        view_employees()
    elif choice == '4':
        clear()
        main_menu()
    else:
        clear()
        view_computer()
        
def view_available_jobs():
    clock(1)
    rj = random_job()
    # print(rj)
    j1 = Job(description=rj['description'], difficulty=rj['difficulty'], reward=rj['reward'], assigned_to=None)
    print(f''' 
        Available Jobs:
            
           | Customer: {fake.name()} 
           | Job Description: {j1.description} 
           | Difficulty: {j1.difficulty} 
           | Reward: {j1.reward}
          ''')
    accept = input('        Accept This Job? (y/n)\n--> ')
    if accept == 'y':
        print('Job Accepted')
        session.add(j1)
        session.commit()
        time.sleep(1)
        clear()
        view_computer()
        view_available_jobs()
    else:
        clear()
        view_computer()
        
def view_resumes():
    clock(1)
    new_mech_level = random.randint(1, 10)
    new_mech_salary = new_mech_level * 150 + 500
    M1 = Mechanic(name=fake.name(), level=new_mech_level, salary=new_mech_salary)
    query = input(f"""
        A Mechanic Wants to Join Your Team!\n
            | Name: {M1.name}
            | Level: {M1.level}
            | Desired salary: {M1.salary}\n
        Hire Mechanic? (y/n) """)
    if query == "y":
        session.add(M1)
        session.commit()
        print(f"{M1.name} has been hired!")
        time.sleep(1)
        clear()
        view_computer()
    else:
        print(f"{M1.name} has been rejected.")
        time.sleep(1)
        clear()
        view_computer()
    
def view_employees():
    clock(1)
    employees = session.query(Mechanic).all()
    print('\nCurrent Employees:\n')
    for employee in employees:
        print(f'''  
  {employee.id} | {employee.name} 
    | Level: {employee.level} 
    | Salary: {employee.salary}\n''')
    fire = input('Would you like to fire an employee? (y/n)\n--> ')
    if fire == 'y':
        selcted_employee = input('Enter the ID of the employee to fire --> ')
        if selcted_employee in [str(employee.id) for employee in employees]:
            session.query(Mechanic).filter(
                Mechanic.id == selcted_employee).delete()
            console.print(f'\n[bright_yellow bold]<---Employee Fired--->[/]\n')
            time.sleep(1)
            clear()
            view_employees()
        else:
            clear()
            view_employees()
    else:
        clear()
        view_computer()
#-------------------END OF COMPUTER FUNCTIONS-------------------#



#-------------------WORKSHOP FUNCTIONS-------------------#
def view_workshop():
    clock(1)
    print('=' * int(terminal_width))
    console.print('''[chartreuse1]

             o 
 cc88b       Cb       __||___________________||_               
68%8QU89    d8Ub    _//=========================\          cce*88oo      
O0896%68Oo   ||   l/=/===========================\      C8O8*8Q8P*Ob o8oo
a%0C88i%8B,,    " /==/=============================\   dOB*9*OLS*UOpugO9*D
PQ%OO8OO' |||, "  |..|     __               __ -=  |-' CO*9O0*89PBCOPL*SOBB*
8OUC%CBO%b`|||,,,,|..| O  |  |   -=-       |  |  O |  " Cgg*bU8*UO*OOd*UOdcb
89Y|//OOP `||||||||..||/| |__| ___________ |__| |/||,,,,,,6O*U  /p  gc*U*dpP
  \||       \||||||:.||/|      |========||      |/||||||||, \\\//  /d*uUP* ,||||||||||||||||||||||||||||||||||||
  |||        `|||||::||/| =-   |========||      |/||||||||||, \\\////_\ ,,||||||||||||||||||||||||||||||||||||||
         "         \:||/|      |.::..::.|| =    |/|||||||||||| |||// ,,,||||||||||||||||||||||||||||||||||||||||
     "     "        \||_|______|........\|______|_||           |||||
          "       "              ........              "     .//||||\   "           "       "       "       "   
              "            "      ........      "                     "              "        "  
            "       "    .         ........              "        "        "       "        "    "
                                    .........     "          "
::::::::::::::::::::::.........................................::::::::::::::::::::::::::::::::::::::::::::::::::

__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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
    clock(2)
    m_id = input('Select a Mechanic to Assign. \nEnter Mechanic ID --> ')
    selected_mechanic = session.query(Mechanic).filter(Mechanic.id == m_id).first()
    print(f"{selected_mechanic.name} has been selected.")
    j_id = input('Select a Job to Assign. \nEnter Job ID --> ')
    selected_job = session.query(Job).filter(Job.id == j_id).first()
    print(f"Job {selected_job.id} has been selected.\n")
    
    if selected_mechanic.level >= selected_job.difficulty:
        chance_of_success = 85
    else: chance_of_success = (selected_mechanic.level / selected_job.difficulty * 100) -5
    
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
                console.print(f'[deep_pink1]{selected_mechanic.name} Has Leveled Up![/]')
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
#-------------------END OF WORKSHOP FUNCTIONS-------------------#

        



#-------------------FINANCE FUNCTIONS-------------------#
def view_finances():
    clock(1)
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
#-------------------END OF FINANCE FUNCTIONS-------------------#
    

# Classes/Tables --------------------------------------------------------------------------------------
class Mechanic(Base):
    __tablename__ = "mechanics"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)
    salary = Column(Integer)
    def __repr__(self):
        return f"'\n'Employee ID: {self.id}'\n' Name: {self.name}'\n' Level: {self.level}'\n' Salary: ${self.salary} '\n'"


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


#----------------------TIME BASED EVENTS----------------------#
def check_day():
    global current_day
    day_of_the_week = days[(game_days % 7) - 1]
    if current_day == day_of_the_week:
        pass
    else:
        if day_of_the_week == 'Monday':
            new_week_summary()
        else: roll_event_dice()    
        current_day = day_of_the_week

        
def new_week_summary():
    print('New week summary')
    
def roll_event_dice():
    dice = random.randint(1, 1000)
    if dice in range(1, 50):
        clear()
        mech_wants_raise()
    elif dice in range(51, 100):
        clear()
        mech_quits()
    elif dice in range (101, 110):
        clear()
        shop_fire()
    else: pass
        
def mech_wants_raise():
    print('''
          
          ''')
    clear()
    main_menu()
    
def mech_quits():
    print('Mech quits')
    
def shop_fire():
    print('Shop fire')
#----------------------END TIME BASED EVENTS----------------------#


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
clear()
main_menu()
# ---------------------------------------------------------------