import random 

s = set()

while len(s) != 7:
    s.add(random.randint(1, 49))

print(*sorted(s))
