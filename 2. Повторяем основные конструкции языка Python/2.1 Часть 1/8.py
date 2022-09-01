n = int(input())
k = int(input())

l = 0

for i in range(1, n + 1):
    l = (l + k) % i

print(l + 1)
