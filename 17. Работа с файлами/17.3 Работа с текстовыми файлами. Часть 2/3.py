with open('lines.txt', 'r') as file:
    lines = list(map(lambda x: x.strip('\n'), file.readlines()))
    print(*filter(lambda x: len(x) == len(max(lines, key=len)), lines), sep='\n')
