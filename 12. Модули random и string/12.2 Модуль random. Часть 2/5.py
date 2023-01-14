import random

letters = list(input())

random.shuffle(letters)

print("".join(letters))
