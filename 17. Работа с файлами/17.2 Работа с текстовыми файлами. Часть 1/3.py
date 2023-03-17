import random

file = open('lines.txt', 'r', encoding='utf-8')

lines = file.readlines()

print(random.choice(lines))

file.close()
