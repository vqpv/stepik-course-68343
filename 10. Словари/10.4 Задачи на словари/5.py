d = {}

for _ in range(int(input())):
    s = input().split()
    for i in range(1, len(s)):
        d[s[i]] = d.get(s[i], s[0])

for _ in range(int(input())):
    print(d[input()])
