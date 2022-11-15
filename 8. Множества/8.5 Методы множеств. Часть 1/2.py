symbols = set()

for _ in range(int(input())):
    for s in input().lower():
        symbols.add(s)

print(len(symbols))
