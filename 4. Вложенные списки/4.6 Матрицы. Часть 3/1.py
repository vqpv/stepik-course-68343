n, m = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
            matrix[i].append("*")
        else:
            matrix[i].append(".")
    print(*matrix[i])
