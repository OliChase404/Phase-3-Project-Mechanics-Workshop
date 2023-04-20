# from mechanics import new_mech_dice_roll


# game_hours = 0
# game_days = game_hours / 8

# def clock(hours):
#     global game_hours
#     game_hours += hours
#     new_mech_dice_roll()


# def new_mech_dice_roll():
#     new_mech_level = random.randint(1, 10)
#     new_mech_salary = new_mech_level * 150 + 500
#     M1 = Mechanic(name=fake.name(), level=new_mech_level,
#                   salary=new_mech_salary)
#     dice = random.randint(1, 10)
#     if dice > 6:
#         query = input(f"""
# A new mechanic wants to join your team.
# Name: {M1.name}
# Level: {M1.level}
# Desired salary: {M1.salary}
# Do you want to hire him? (y/n) """)
#         if query == "y":
#             session.add(M1)
#             session.commit()
#             print(f"{M1.name} has been hired!")
#         else:
#             print(f"{M1.name} has been rejected.")