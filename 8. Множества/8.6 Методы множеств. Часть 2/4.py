n = int(input())

s = set(input())

for _ in range(n - 1):
    s &= set(input())

print(*sorted(s, key=int))
