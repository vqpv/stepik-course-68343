n, m = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        num = (i + j) % m + 1
        matrix[i].append(num)

for i_2 in range(n):
    print(*matrix[i_2])
