def pretty_print(data, side="-", delimiter="|"):
    s = delimiter + delimiter.join(map(lambda x: " " + str(x) + " ", data)) + delimiter
    a_side = " " + side * (len(s) - 2) + " "
    
    print(f"{a_side}\n{s}\n{a_side}")
