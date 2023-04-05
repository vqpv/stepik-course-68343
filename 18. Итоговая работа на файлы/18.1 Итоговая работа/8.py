with open(input(), 'r') as input_file:
    lines = input_file.read().split('\n')
    f_lines = list(filter(lambda x: "#" in x or "def" in x, lines))
    result = [j[j.find(' ') + 1:j.find("(")] for i, j in enumerate(f_lines) if "def" in j and "#" not in f_lines[i - 1]]
    
    if result:
        print(*result, sep="\n")
    else:
        print("Best Programming Team")
