text = f'{input()} запретил букву '

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

for i in alphabet:
    if i in text:
        print(text + i)
        text = text.replace(i, "").replace("  ", " ").lstrip()
