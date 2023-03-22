with open('numbers.txt', 'r') as file:
    nums_sum = list(map(lambda x: sum(map(int, x.split())), file.readlines()))
    print(*nums_sum, sep='\n')
