d = {}

for _ in range(int(input())):
    i, j = input().split()
    d[i] = d.get(i, j)
    d[j] = d.get(j, i)

print(d[input()])
