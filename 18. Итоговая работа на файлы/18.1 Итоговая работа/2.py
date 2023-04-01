with open('ledger.txt', 'r') as input_file:
    lines = input_file.read().split('\n')
    nums_sum = sum(map(lambda x: int(x.lstrip("$")), lines))
    print(f'${nums_sum}')
