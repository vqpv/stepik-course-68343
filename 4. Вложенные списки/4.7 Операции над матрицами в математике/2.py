n_1, m_1 = map(int, input().split())
matrix_1 = [list(map(int, input().split())) for _ in range(n_1)]

input()

n_2, m_2 = map(int, input().split())
matrix_2 = [list(map(int, input().split())) for _ in range(n_2)]

matrix_3 = [[0] * m_2 for _ in range(n_1)]

for i in range(n_1):
    for j in range(m_2):
        for z in range(m_1):
            matrix_3[i][j] += matrix_1[i][z] * matrix_2[z][j]

for i_2 in range(n_1):
    print(*matrix_3[i_2])
