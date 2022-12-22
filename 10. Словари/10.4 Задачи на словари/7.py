cipher = input()

d_1 = {}
d_2 = {}

for c_1 in cipher:
    d_1[c_1] = d_1.get(c_1, 0) + 1

for _ in range(int(input())):
    i, j = input().split(": ")
    d_2[int(j)] = d_2.get(int(j), i)

for c_2 in cipher:
    print(d_2[d_1[c_2]], end="")
