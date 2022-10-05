n, m = map(int, input().split())

matrix = []
c = 1

for i in range(n):
    matrix.append([])
    for _ in range(m):
        matrix[i].append(c)
        print(c, end=" ")
        c += 1
    print()
