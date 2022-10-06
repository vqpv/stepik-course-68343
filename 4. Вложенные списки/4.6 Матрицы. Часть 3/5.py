n = int(input())

matrix = [[0 for i in range(n)] for _ in range(n)]

for i in range(n):
    for _ in range(n):
        matrix[i][i] = 1
        matrix[i][n - i - 1] = 1
        
for i_2 in range(n):
    print(*matrix[i_2])
