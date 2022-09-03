nums = list(map(int, input().split()))

c = 0

for i in range(len(nums) - 1):
    if nums[i] < nums[i + 1]:
        c += 1

print(c)
