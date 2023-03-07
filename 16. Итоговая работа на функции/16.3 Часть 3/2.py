from functools import reduce

def product_of_odds(data):
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)
