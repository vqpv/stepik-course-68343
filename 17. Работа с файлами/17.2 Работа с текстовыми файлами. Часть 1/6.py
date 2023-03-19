file = open('prices.txt', 'r', encoding='utf-8')

prices = file.readlines()

print(sum(map(lambda x: int(x[1]) * int(x[2]), [i.split() for i in prices])))

file.close()
