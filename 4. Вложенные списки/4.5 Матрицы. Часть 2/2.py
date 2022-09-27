n, m = int(input()), int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]
r, c = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[r][c]:
            r, c = i, j

print(r, c)
