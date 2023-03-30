for _ in range(int(input())):
    with open(input(), 'r') as input_file, open('output.txt', 'a') as output_file:
        output_file.write(input_file.read())
