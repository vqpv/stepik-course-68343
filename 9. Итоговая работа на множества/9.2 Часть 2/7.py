m, n = int(input()), int(input())

s_1 = {input() for i in range(m)}
s_2 = {input() for i in range(n)}

print(len(s_1 - s_2))
