d = {}

for _ in range(int(input())):
    i, j = input().split(": ")
    d[i.lower()] = d.get(i, j)

for _ in range(int(input())):
    print(d.get(input().lower(), "Не найдено"))
