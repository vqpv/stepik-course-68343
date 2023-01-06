def merge(values):
    d = {}
    for value in values:
        for k, v in value.items():
            d.setdefault(k, set()).add(v)
    return 
