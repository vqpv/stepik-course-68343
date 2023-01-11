import random

def generate_ip():
    nums = [str(random.randint(0, 255)) for i in range(4)]
    return ".".join(nums)
