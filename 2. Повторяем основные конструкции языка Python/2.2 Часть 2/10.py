word = "anton"

lst = []

for i in range(int(input())):
    s = input()
    c = 0
    for w in word:
        if w in s:
            c += 1
            s = s[s.find(w):]
    if c == len(word):
        lst.append(i + 1)

print(*lst)
