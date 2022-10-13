from copy import deepcopy

n = int(input())
matrix_1 = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

matrix_2 = deepcopy(matrix_1)

for _ in range(m - 1):
    matrix_3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for z in range(n):
                matrix_3[i][j] += matrix_1[i][z] * matrix_2[z][j]
    matrix_1 = deepcopy(matrix_3)

for i_2 in range(n):
    print(*matrix_3[i_2])
