n = int(input()) + 1

print(*[[i for i in range(1, j + 1)] for j in range(1, n)], sep='\n')
