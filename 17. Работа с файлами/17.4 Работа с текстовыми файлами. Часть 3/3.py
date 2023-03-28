with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    text = input_file.read().split()
    output_file.writelines([f'{i}) {j}\n' for i, j in enumerate(text, 1)])
