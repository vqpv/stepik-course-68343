import string
import random

def generate_password(length):
    symbols = [i for i in (string.ascii_letters + string.digits) if i not in "lI1oO0"]
    return "".join([random.choice(symbols) for i in range(length)])

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())

generate_passwords(n, m)
