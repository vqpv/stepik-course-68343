def print_products(*args):
    products = [i for i in args if i and isinstance(i, str)]
    if products:
        for i, j in enumerate(products):
            print(f"{i + 1}) {j}")
    else:
        print("Нет продуктов")
