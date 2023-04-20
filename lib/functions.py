import random

def random_job():
    all_jobs = [
        {'description': 'Refill Blinker Fluid', 'difficulty': 10, 'reward': 6000},
        {'description': 'Recharge AC', 'difficulty': 5, 'reward': 700},
        {'description': 'Remove Raccoon', 'difficulty': 7, 'reward': 1000},
        {'description': 'Oil Change', 'difficulty': 1, 'reward': 150},
        {'description': 'Install New Tires', 'difficulty': 4, 'reward': 900},
        {'description': 'Remap ECU', 'difficulty': 8, 'reward': 1500},
        {'description': 'Replace Shock Absorbers', 'difficulty': 6, 'reward': 2000},
        ]
    return random.choice(all_jobs)