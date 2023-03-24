with open('population.txt', 'r') as file:
    lines = file.read().split('\n')
    filter_lines = filter(lambda x: x[0].startswith("G") and int(x[1]) >= 500000, list(map(lambda x: x.split('\t'), lines)))
    countries = list(map(lambda x: x[0], filter_lines))
    print(*countries, sep="\n")
