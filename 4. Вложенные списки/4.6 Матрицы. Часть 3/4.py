n, m = map(int, input().split())

matrix = [[0 for i in range(m)] for _ in range(n)]
c = 1

for i in range(m):
    for j in range(n):
        matrix[j][i] = c
        c += 1

for i_2 in range(n):
    print(*matrix[i_2])
