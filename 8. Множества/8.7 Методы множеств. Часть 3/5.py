s_1, s_2, s_3 = set(input().split()), set(input().split()), set(input().split())

print(*sorted(s_3 - s_2 - s_1, reverse=True, key=int))
