string = [i.strip('.,!?:;-').lower() for i in input().split()]

result = {}

for word in string:
    result[word] = result.get(word, 0) + 1

print(min(sorted(result), key=result.get))
