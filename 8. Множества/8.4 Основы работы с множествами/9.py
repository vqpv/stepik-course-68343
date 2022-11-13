s_1, s_2, s_3 = input().split()

print("YES" if set(s_1) == set(s_2) and set(s_1) == set(s_3) else "NO")
