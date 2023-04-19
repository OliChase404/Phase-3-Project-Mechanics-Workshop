from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from ipdb import set_trace
from faker import Faker
import os

engine = create_engine("sqlite:///workshop.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

fake = Faker()

from jobs import Job
from mechanics import Mechanic

workshop_funds = 10000
fund_ticker = f'|-->Current funds: ${workshop_funds}<--|'


def main_menu():
    terminal_width = os.get_terminal_size().columns
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
          \__\/  \:\      \~~\:\   \  \:\  /:/   \  \:\  /:/   \  \:\  /:/   \  \:\  ~~~                    
               \  \:\      \  \:\   \  \:\/:/     \  \:\/:/     \  \:\/:/     \  \:\                        
                \__\/       \__\/    \  \::/       \  \::/       \  \::/       \  \:\                       
                                      \__\/         \__\/         \__\/         \__\/  

      """)
    print('🔧' * int(terminal_width / 2))
    print(f'\n{" " * int((terminal_width / 2) - (len(fund_ticker) / 2))}{fund_ticker}\n')

    print("""
          Choose an option:
            1. Hire a mechanic
            
          """)
    









main_menu()

