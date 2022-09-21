n, m = int(input()), int(input())

matrix = []

for i in range(n):
    matrix.append([])
    for _ in range(m):
        matrix[i].append(input())
    print(*matrix[i])
