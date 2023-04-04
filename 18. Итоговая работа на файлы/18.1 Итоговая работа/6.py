import re

with open(input(), 'r') as input_file_1, open('forbidden_words.txt', 'r') as input_file_2:
    text = input_file_1.read()
    words = input_file_2.read().split(' ')

    for word in words:
        text = re.sub(word, "*" * len(word), text, flags=re.IGNORECASE)

    print(text)
