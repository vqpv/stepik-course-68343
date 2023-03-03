all_c = []

for _ in range(int(input())):
    c = []
    for _ in range(int(input())):
        c.append(input().split()[1] == str(5))
    all_c.append(any(c))

print("YES" if all(all_c) else "NO")
