from fractions import Fraction
from math import gcd

num = int(input())

num_2 = (num // 2) + 1
num_3 = num - num_2

while gcd(num_2, num_3) != 1:
    num_2 += 1
    num_3 -= 1

print(Fraction(num_3, num_2))
