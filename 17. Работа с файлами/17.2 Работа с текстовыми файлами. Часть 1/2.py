file = open(input(), 'r', encoding='utf-8')

lines = file.readlines()

print(lines[-2])

file.close()
