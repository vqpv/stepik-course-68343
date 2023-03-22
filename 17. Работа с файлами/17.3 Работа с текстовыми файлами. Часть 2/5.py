import re

with open('nums.txt', 'r') as file:
    print(sum(map(int, re.sub(r'[^0-9]', ' ', file.read()).split())))
