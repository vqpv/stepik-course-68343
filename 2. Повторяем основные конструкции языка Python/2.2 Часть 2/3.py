nums = list(map(int, input().split()))

n_1 = nums[::2]
c = 0

for i in nums[1::2]:
    n_1.insert(c, i)
    c += 2

print(*n_1)
