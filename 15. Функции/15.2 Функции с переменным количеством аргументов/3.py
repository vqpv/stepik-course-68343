def mean(*args):
    nums = [i for i in args if type(i) in (float, int)]
    if nums:
        return sum(nums) / len(nums)
    return 0
