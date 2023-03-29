with open('goats.txt', 'r') as input_file, open('answer.txt', 'w') as output_file:
    s_text = input_file.read().split('\nGOATS\n')
    colours = s_text[0].lstrip('COLOURS\n').split('\n')
    goats = [i for i in s_text[1].split('\n') if i in colours]

    print(*[c for c in colours if round((goats.count(c) / len(goats)) * 100) > 7], sep='\n', file=output_file)
