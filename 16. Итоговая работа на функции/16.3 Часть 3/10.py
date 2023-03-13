def gem(word):
    return sum(map(lambda c: ord(c) - ord("A"), word.upper()))

print(*sorted([input() for _ in range(int(input()))], key=lambda x: (gem(x), x)), sep="\n")
