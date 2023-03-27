from random import sample

with open('random.txt', 'w', encoding='utf-8') as file:
    print(*sample(range(111, 777), 25), sep='\n', file=file)
