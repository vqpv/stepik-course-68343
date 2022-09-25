matrix = []
q_1, q_2, q_3, q_4 = 0, 0, 0, 0

n = int(input())
for i in range(n):
    s = input().split()
    for i_2, j_2 in enumerate(s):
        if i < i_2 and i < n - 1 - i_2:
            q_1 += int(j_2)
        elif i < i_2 and i > n - 1 - i_2:
            q_2 += int(j_2)
        elif i > i_2 and i > n - 1 - i_2:
            q_3 += int(j_2)
        elif i > i_2 and i < n - 1 - i_2:
            q_4 += int(j_2)
    matrix.append(s)

print("Верхняя четверть:", q_1)
print("Правая четверть:", q_2)
print("Нижняя четверть:", q_3)
print("Левая четверть:", q_4)
