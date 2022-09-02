q_1, q_2, q_3, q_4 = 0, 0, 0, 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        q_1 += 1
    elif x < 0 and y > 0:
        q_2 += 1
    elif x < 0 and y < 0:
        q_3 += 1
    elif x > 0 and y < 0:
        q_4 += 1

print("Первая четверть:", q_1)
print("Вторая четверть:", q_2)
print("Третья четверть:", q_3)
print("Четвертая четверть:", q_4)
