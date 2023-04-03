with open(input(), 'r') as input_file:
    lines = []
    for line in input_file:
        lines.append(line.strip())
        if len(lines) > 10:
            del lines[0]
    
    print(*lines, sep='\n')
