with open('data.txt', 'r') as file:
    print(*(map(lambda x: x.strip("\n"), file.readlines()[::-1])), sep="\n")
