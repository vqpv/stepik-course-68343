chars = list(input().split())

lst = []

for c in chars:
    if lst and c in lst[-1]:
        lst[-1].append(c)
    else:
        lst.append([c])

print(lst)
