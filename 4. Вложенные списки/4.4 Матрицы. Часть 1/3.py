matrix = []
c, s = 0, 0

for _ in range(int(input())):
    matrix.append(input().split())

for i, _ in enumerate(matrix):
    s += int(matrix[i][c])
    c += 1

print(s)
