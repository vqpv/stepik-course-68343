p = {"read": "R", "write": "W", "execute": "X"}

files = {i[0]: i[1:] for i in [input().split() for _ in range(int(input()))]}

for _ in range(int(input())):
    c = input().split()
    print("OK" if p[c[0]] in files[c[1]] else "Access denied")
