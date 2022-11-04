n = int(input())

t_1 = t_2 = t_3 = 1

for _ in range(n):
    print(t_1, end=" ")
    t_1, t_2, t_3 = t_2, t_3, t_1 + t_2 + 
