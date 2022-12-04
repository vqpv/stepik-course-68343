m, n = int(input()), int(input())

s_1 = {input() for i in range(m)}
s_2 = {input() for i in range(n)}

s_3 = s_1 ^ s_2

print(len(s_3) if s_3 else "NO")
