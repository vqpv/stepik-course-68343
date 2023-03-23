with open('file.txt', 'r') as file:
    text = file.read()
    letters = len(list(filter(lambda x: x.isalpha(), text)))
    words = len(text.split())
    lines = len(text.split('\n'))

    print(f'Input file contains:\n{letters} letters\n{words} words\n{lines} lines')
