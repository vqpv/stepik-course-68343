chars = input().split()
n = int(input())

lst = []

for i in range(0, len(chars), n):
    lst.append(chars[i:i + n])

print(lst)
