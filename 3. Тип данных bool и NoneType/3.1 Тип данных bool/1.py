# объявление функции
def func(num_1, num_2):
    return num_1 % num_2 == 0

# считываем данные
num_1, num_2 = int(input()), int(input())

# вызываем функцию
if func(num_1, num_2):
    print("делится")
else:
    print("не делится")
