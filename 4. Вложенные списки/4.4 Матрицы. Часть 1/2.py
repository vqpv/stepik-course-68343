n, m = int(input()), int(input())

matrix = []

for i in range(n):
    matrix.append([])
    for _ in range(m):
        matrix[i].append(input())
    print(*matrix[i])

print()

for i_2 in range(m):
    for j_2 in range(n):
        print(matrix[j_2][i_2], end=' ')
    print()
