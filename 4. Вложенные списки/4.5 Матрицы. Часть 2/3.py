n, m = int(input()), int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]
r, c = map(int, input().split())

for i in range(n):
    matrix[i][r], matrix[i][c] = matrix[i][c], matrix[i][r]
    print(*matrix[i])
