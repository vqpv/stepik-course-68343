import random

def generate_index():
    index = ""
    for idx in range(6):
        if idx == 2:
            index += str(random.randint(0, 99)) + "_"
        elif idx == 3:
            index += str(random.randint(0, 99))
        else:
            index += chr(random.randint(65, 90))
    return index
