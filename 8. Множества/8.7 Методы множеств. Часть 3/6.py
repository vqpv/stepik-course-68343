s_1, s_2, s_3 = set(input().split()), set(input().split()), set(input().split())

s_4 = set(str(i) for i in range(11))

print(*sorted(s_4 - (s_1 | s_2 | s_3), key=int))
