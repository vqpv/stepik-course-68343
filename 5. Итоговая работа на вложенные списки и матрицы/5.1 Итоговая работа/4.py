n = int(input())

matrix = [["."] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1 or i == n // 2 or j == n // 2:
            matrix[i][j] = "*"

for i_2 in range(n):
    print(*matrix[i_2])
