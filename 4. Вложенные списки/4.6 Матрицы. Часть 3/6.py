n = int(input())

matrix = [[1 for i in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i > j and i + 1 + j < n) or (i < j and i + 1 + j > n):
            matrix[i][j] = 0
            matrix[i][j] = 0
        
for i_2 in range(n):
    print(*matrix[i_2])
