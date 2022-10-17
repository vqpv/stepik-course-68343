n = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix.reverse()
result = "YES"

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            result = "NO"

print(result)
