with open('logfile.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    text = input_file.read().split('\n')
    users = [i.split(', ') for i in text]
    users_m = map(lambda x: [x[0], int(x[1].split(':')[0]) * 60 + int(x[1].split(':')[1]), int(x[2].split(':')[0]) * 60 + int(x[2].split(':')[1])], users)
    print(*[i[0] for i in users_m if i[2] - i[1] >= 60], sep='\n', file=output_file)
