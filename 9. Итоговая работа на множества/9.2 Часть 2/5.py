nums_1 = set(input().split())
nums_2 = set(input().split())

same_nums = nums_1 & nums_2

if same_nums:
    print(*sorted(same_nums, reverse=True, key=int))
else:
    print("BAD DAY")
