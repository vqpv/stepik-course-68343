file = open('nums.txt', 'r', encoding='utf-8')

numbers = file.read()

print(sum(map(int, numbers.split())))

file.close()
