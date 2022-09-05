nums = list(map(int, input().split()))

nums.insert(0, nums[-1])
nums.pop(-1)

print(*nums)
