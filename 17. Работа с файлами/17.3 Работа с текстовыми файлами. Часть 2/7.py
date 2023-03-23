import random

with open('first_names.txt', 'r') as file_1, open('last_names.txt', 'r') as file_2:
    first_names = file_1.read().split()
    last_names = file_2.read().split()
    for _ in range(3):
        print(f'{random.choice(first_names)} {random.choice(last_names)}')
