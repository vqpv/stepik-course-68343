password = input()

if len(password) >= 7 and any(map(lambda x: x.islower(), password)) and any(map(lambda x: x.isupper(), password)) and any(map(lambda x: x.isdigit(), password)):
    print("YES")
else:
    print("NO")
