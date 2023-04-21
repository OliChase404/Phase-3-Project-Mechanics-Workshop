# Autoshop Tycoon
## Summary

This application utilizes SQLAlchemy and database management to create an interactive CLI where users can manage their very own autoshop.

## How to play

To run the program and play the game, the following commands must be run in the *Phase-3-Project-Mechanics-Workshop* directory:
```
pipenv install
pipenv shell
python lib/game.py 

```
The user will then be transported to the Main Menu where they will be presented with the following options:
1. View Computer
2. View Workshop
3. Visit Bank

To play the game, follow the prompts provided within each of these options. However, before selecting an option, remember, **YOU ARE THE MANAGER**, and **EVERY** decision matters. Note that at the top of the *Main Menu* screen, both the current day and your shop's current funds are displayed. Allocate these funds to hire new mechanics, pay customers for failed repairs, and most importantly, **TO KEEP YOUR AUTOSHOP AFLOAT**! With every decision made, time passes. At the end of the week, you will be charged for the upkeep of your autoshop. **DON'T RUN OUT OF MONEY!**

To make money, you must complete jobs. In order to get jobs, you must accept them at your computer. Every job has a difficulty rating and an associated compensation upon completion. As a manager, it's important to select your jobs based on the quality of your mechanics or else you may end up losing all your money having to paying for additional damages caused by the failures of your employees. As mechanics complete jobs, their competency will increase. Keep in mind, if you're ever unsatisfied by the performance of your current employees, you have the option fire existing mechanics and hire new mechanics. 


## Under the hood

This application utilizes SQLAlchemy to create a *workshop* database. This database stores three tables: Mechanics, Jobs, and Finances. A representation of the columns is shown below:
### Mechanics Table
| Column|Type|
|-----|-------|       
|id|primary integer|
| name|String|
| level|Integer|
| salary|Integer|

### Jobs Table
| Column|Type|
|-----|-------|       
|id|primary integer|
|description|String|
|difficulty|Integer|
|reward|Integer|
|assigned_to|Integer|

### Finance Table
| Column|Type|
|-----|-------|       
|id|primary integer|
|Current Funds|Integer|
|Income This Week|Integer|
|Shop Upkeep|Integer|
|Total Salaries|Integer|

Utilizing sessionmaker within SQLAlchemy, the code is able to constantly obtain information from these tables, as well as update the database as the game progresses. 

Additional resources used in this application were Faker's python package and Rich's python library. 
- [Faker Python Package](https://faker.readthedocs.io/en/master/)
- [Rich Python Library](https://rich.readthedocs.io/en/stable/introduction.html)

Faker is an incredibly useful resource that was used to help generate random occurances such as the names for the mechanics. 

The Rich library was used to help style the the text shown in the terminal within the application.
