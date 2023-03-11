from operator import add, sub, mul, truediv

k = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv
}

def arithmetic_operation(operation):
    def func(x, y):
        return k[operation](x, y)
    return func
