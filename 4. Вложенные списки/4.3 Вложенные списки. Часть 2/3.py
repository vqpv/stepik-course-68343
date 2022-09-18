num = int(input())

lst_1 = [1]

if num != 0:
    for _ in range(num):
        lst_2 = lst_1.copy()
        lst_3 = []
        lst_1.pop(0)
        lst_2.pop(-1)
        for i, j in enumerate(lst_1):
            lst_3.append(j + lst_2[i])
        lst_3.insert(0, 1)
        lst_1 = lst_3 + [1]

print(lst_1)
