w, h = float(input()), float(input())

w_index = w / (h * h)

if w_index < 18.5:
    print("Недостаточная масса")
elif w_index > 25:
    print("Избыточная масса")
else:
    print("Оптимальная масса")
