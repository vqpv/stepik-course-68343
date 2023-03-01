abscissas = [i for i in input().split()]
ordinates = [i for i in input().split()]
applicates = [i for i in input().split()]

print(all(map(lambda i: float(i[0]) ** 2 + float(i[1]) ** 2 + float(i[2]) ** 2 <= 2 ** 2, zip(abscissas, ordinates, applicates))))
