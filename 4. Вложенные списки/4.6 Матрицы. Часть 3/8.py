n, m = map(int, input().split())

matrix = [[0 for i in range(m)] for j in range(n)]
c = 0

for i in range(n):
    for j in range(m):
        c += 1
        matrix[i][j] = c

for i_2 in range(n):
    if i_2 % 2 == 1:
        print(*reversed(matrix[i_2]))
    else:
        print(*matrix[i_2])
