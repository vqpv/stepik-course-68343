letters = input().lower().split()

result = {}

for char in letters:
    if char in result:
        count = result.get(char)
        print(f"{char}_{count}", end=" ")
    else:
        print(char, end=" ")
    result[char] = result.get(char, 0) + 1
