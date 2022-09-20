chars = input().split()

lst = [[]]

for i in range(len(chars) + 1):
    for j in range(len(chars)):
        new_lst = chars[j:j + i + 1]
        if len(new_lst) == i + 1:
            lst.append(new_lst)
print(lst)
