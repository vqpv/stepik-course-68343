with open('class_scores.txt', 'r') as input_file, open('new_scores.txt', 'w') as output_file:
    text = [i.split() for i in input_file.read().split('\n')]
    print(*map(lambda x: f'{x[0]} {int(x[1]) + 5}' if int(x[1]) < 96 else f'{x[0]} 100', text), sep='\n', file=output_file)
