from fractions import Fraction
from math import factorial

s = 0

for i in range(1, int(input()) + 1):
    s += Fraction(1, factorial(i))

print(s)
