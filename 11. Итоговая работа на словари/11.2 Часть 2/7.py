d = {}

for _ in range(int(input())):
    a, b, c = input().split()
    d.setdefault(a, {})
    d[a][b] = d[a].get(b, 0) + int(c)

for key, value in sorted(d.items()):
    print(f'{key}:')
    for k, v in sorted(value.items()):
        print(k, v)
