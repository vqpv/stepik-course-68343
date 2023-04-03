with open('words.txt', 'r') as input_file:
    words = input_file.read().split(' ')
    print(*filter(lambda x: len(x) == len(max(words, key=len)), words), sep='\n')
