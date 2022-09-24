matrix = []
new_lst = []

n = int(input())
for i in range(n):
    s = input().split()
    for i_2, j_2 in enumerate(s):
        if i >= i_2 and (i <= n - 1 - i_2 or i >= n - 1 - i_2):
            new_lst.append(int(j_2))
    matrix.append(s)

print(max(new_lst))
