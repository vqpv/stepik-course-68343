n = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

matrix.reverse()

for i in range(n):
    print(*matrix[i])
