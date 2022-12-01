n = int(input())

cities = {input()}
answer = "OK"

for _ in range(n):
    city = input()
    if city in cities:
        answer = "REPEAT"
        break
    else:
        cities.add(city)

print(answer)
