d = {}

for _ in range(int(input())):
    i, j = input().split()
    d[j.lower()] = d.get(j.lower(), []) + [i]

for _ in range(int(input())):
    print(*d.get(input().lower(), ["абонент не найден"]))
