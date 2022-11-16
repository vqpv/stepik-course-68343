s = [i.lower().strip('.,;:-?!') for i in input().split()]

print(len(set(s)))
