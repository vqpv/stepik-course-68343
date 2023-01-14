import random

numbers = set()

while len(numbers) != 100:
    numbers.add(random.randint(1000000, 9999999))

print(*numbers, sep="\n")
