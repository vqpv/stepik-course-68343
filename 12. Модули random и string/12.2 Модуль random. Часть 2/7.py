import random

n = int(input())

names_1 = [input() for _ in range(n)]
step = random.randint(1, n - 1)

names_2 = names_1[-step:] + names_1[:-step]

for i in range(n):
    print(f"{names_1[i]} - {names_2[i]}")
