def read_csv():
    with open('data.csv', 'r') as file:
        r = []
        keys = file.readline().rstrip().split(",")
        all_data = list(map(lambda x: x.rstrip().split(","), file.readlines()))
        for d in all_data:
            r.append(dict(zip(keys, d)))

    return r
