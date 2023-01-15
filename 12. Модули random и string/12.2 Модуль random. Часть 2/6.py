import random

matrix = []
numbers = set()

for _ in range(5):
    row = []
    for _ in range(5):
        num = random.randint(1, 75)
        while num in numbers:
            num = random.randint(1, 75)
        numbers.add(num)
        row.append(num)
    matrix.append(row)

matrix[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(matrix[i][j]).ljust(3), end="")
    print()
