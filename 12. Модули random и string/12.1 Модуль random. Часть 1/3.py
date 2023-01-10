import random

length = int(input())    # длина пароля

for _ in range(length):
    print(random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))]), end="")
