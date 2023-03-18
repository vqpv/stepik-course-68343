file = open('numbers.txt', 'r', encoding='utf-8')

numbers = file.readlines()

print(sum(map(int, numbers)))

file.close()
