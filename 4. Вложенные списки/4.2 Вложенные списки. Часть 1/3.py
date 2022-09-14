list_1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

for lst in list_1:
    if maximum < max(lst):
        maximum = max(lst)

print(maximum)
