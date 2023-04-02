with open('grades.txt', 'r') as input_file:
    lines = input_file.readlines()
    print(len([i for i in lines if all(map(lambda x: int(x) >= 65, i.split()[1:]))]))
