n = int(input())

lst = list(range(1, n + 1))
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix_t = [[0] * n for _ in range(n)]
result = "YES"

for i in range(n):
    for j in range(n):
        matrix_t[i][j] = matrix[j][i]

for i_2 in range(n):
    if sorted(matrix[i_2]) != lst or sorted(matrix_t[i_2]) != lst:
        result = "NO"
        break

print(result)
