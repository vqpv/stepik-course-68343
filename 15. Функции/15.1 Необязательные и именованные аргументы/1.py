def matrix(n=1, m=None, value=0):
    if not m:
        m = n
    return [[value] * m for _ in range(n)]
