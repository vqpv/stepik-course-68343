n = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[-i - 1][i] = matrix[-i - 1][i], matrix[i][i]

for i_2 in range(n):
    print(*matrix[i_2])
