n = int(input())

matrix = [[0 for i in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            matrix[i][j] = 1
        if i + j >= n:
            matrix[i][j] = 2

for i_2 in range(n):
    print(*matrix[i_2])
