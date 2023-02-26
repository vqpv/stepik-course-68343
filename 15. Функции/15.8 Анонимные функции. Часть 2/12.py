from functools import reduce

evaluate = lambda nums, x: reduce(lambda a_1, b_1: a_1 + b_1, map(lambda a_2, b_2: int(a_2) * (x ** b_2), nums, reversed(range(len(nums)))), 0)

print(evaluate(input().split(), int(input())))
