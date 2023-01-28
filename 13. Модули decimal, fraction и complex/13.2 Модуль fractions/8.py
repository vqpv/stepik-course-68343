from fractions import Fraction
from math import gcd

n = int(input())
s = set()

for i in range(1, n):
    for j in range(2, n + 1):
        if gcd(i, j) == 1 and i < j:
            s.add(Fraction(i, j))

print(*sorted(s), sep="\n")
