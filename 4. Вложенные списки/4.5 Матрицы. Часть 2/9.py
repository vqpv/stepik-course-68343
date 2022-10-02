n = int(input())

need_nums = set(range(1, n ** 2 + 1))
matrix = [[int(i) for i in input().split()] for _ in range(n)]

nums = set()
result = "NO"
r_1, r_n = 0, 0
c_1, c_n = 0, 0
d = 0

for i in range(n):
    nums.update(matrix[i])
    for j in range(n):
        if i == 0:
            r_1 += matrix[i][j]
        if i == n - 1:
            r_n += matrix[i][j]
        if j == 0:
            c_1 += matrix[i][j]
        if j == n - 1:
            c_n += matrix[i][j]
        if i == j:
            d += matrix[i][j]
        

if nums == need_nums:
    if r_1 == r_n and c_1 == c_n and d == r_1 and r_1 == c_1:
        result = "YES"

print(result)
