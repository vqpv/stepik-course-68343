d_1 = {}
d_2 = {}

for i in input():
    d_1[i] = d_1.get(i, 0) + 1

for j in input():
    d_2[j] = d_2.get(j, 0) + 1

print("YES" if d_1 == d_2 else "NO")
