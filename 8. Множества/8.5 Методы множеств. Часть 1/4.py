nums = input().split()

new_nums = set()

for n in nums:
    n = n.lstrip('0')
    if n in new_nums:
        print('YES')
    else:
        print('NO')
        new_nums.add(n)
