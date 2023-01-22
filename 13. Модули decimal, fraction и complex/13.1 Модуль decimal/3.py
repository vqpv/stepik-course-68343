from decimal import Decimal

num = Decimal(input())

num_tuple = num.as_tuple().digits

print(max(num_tuple) if int(num) == 0 else max(num_tuple) + min(num_tuple))
