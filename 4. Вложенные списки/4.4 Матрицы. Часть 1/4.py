matrix = []

for _ in range(int(input())):
    s = list(map(int, input().split()))
    c = 0
    for i in s:
        if i > sum(s) / len(s):
            c += 1
    print(c)
    matrix.append(s)
