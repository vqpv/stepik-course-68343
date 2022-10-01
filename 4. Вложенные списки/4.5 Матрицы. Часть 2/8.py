coordinates = input()

r = "87654321".index(coordinates[1])
c = "abcdefgh".index(coordinates[0])

matrix = [["." for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):
        if abs((r - j) * (c - i)) == 2:
            matrix[j][i] = "*"

matrix[r][c] = "N"

for i_2 in range(8):
    print(*matrix[i_2])
