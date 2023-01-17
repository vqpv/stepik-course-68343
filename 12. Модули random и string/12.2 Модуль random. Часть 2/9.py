import string
import random

def generate_password(length):
    digits = [i for i in string.digits if i not in "01"]
    upper = [i for i in string.ascii_uppercase if i not in "OI"]
    lower = [i for i in string.ascii_lowercase if i not in "ol"]
    symbols = digits + upper + lower
    password_symbols = list(random.choice(digits) + random.choice(upper) + random.choice(lower)) + [random.choice(symbols) for i in range(length - 3)]
    random.shuffle(password_symbols)
    return "".join(password_symbols)

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())

generate_passwords(n, m)
