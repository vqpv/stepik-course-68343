n, m = map(int, input().split())

matrix_1 = [list(map(int, input().split())) for _ in range(n)]

input()

matrix_2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(matrix_1[i][j] + matrix_2[i][j], end=" ")
    print()
