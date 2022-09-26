n, m = int(input()), int(input())

matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(i * j)
    print(*matrix[i])
