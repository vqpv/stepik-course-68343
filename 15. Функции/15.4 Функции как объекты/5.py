from math import sin

def f_1(n):
    return n ** 2

def f_2(n):
    return n ** 3

def f_3(n):
    return n ** 0.5

def f_4(n):
    return abs(n)

def f_5(n):
    return sin(n)

commands = {'квадрат': f_1, 'куб': f_2, 'корень': f_3, 'модуль': f_4, 'синус': f_5}

num = int(input())
command = input()

print(commands[command](num))
