nums = input().split()

def sort_by_sum(num):
    return sum([int(i) for i in num]), int(num)

print(*sorted(nums, key=sort_by_sum))
