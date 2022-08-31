num = input()

if len(num) == 5:
    print(int(num[::-1]))
else:
    print(int(num[0] + num[1:][::-1]))
