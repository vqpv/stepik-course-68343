n, m = map(int, input().split())

matrix = [[0 for i in range(m)] for j in range(n)]
c_1 = 0
c_2 = 1

for i in range(n):
    for j in range(m):
        c_1 += 1
        matrix[i][j] = c_1

for z in range(n + m):
    for i_2 in range(n):
        for j_2 in range(m):
            if z == i_2 + j_2:
                matrix[i_2][j_2] = c_2
                c_2 += 1

for i_3 in range(n):
    print(*matrix[i_3])
