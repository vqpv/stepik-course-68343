from fractions import Fraction

s = 0

for i in range(1, int(input()) + 1):
    s += Fraction(1, i ** 2)

print(s)
