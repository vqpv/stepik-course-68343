def greet(name, *args):
    names = list(args)
    names.insert(0, name)
    r = " and ".join(names)
    return f"Hello, {r}!"
