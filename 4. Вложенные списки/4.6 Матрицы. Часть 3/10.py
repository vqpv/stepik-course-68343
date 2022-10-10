n, m = map(int, input().split())

if n == 1:
    matrix = [list(range(1, m + 1))]

elif m == 1:
    matrix = [[i] for i in range(1, n + 1)]

else:
    if n > m:
        k = m
    else:
        k = n

    # Генерация пустой матрицы:
    matrix = [[0] * m for i in range(n)]

    # Счетчик чисел:
    c = 1

    # Счетчик для первой строки:
    c_1 = 0

    # Центр матрицы:
    matrix[n // 2][m // 2] = n ** 2

    # Цикл матрицы:
    for i in range(k // 2):

        # Верхняя горизонталь:
        for j_1 in range(m - c_1):
            matrix[i][j_1 + i] = c
            c += 1

        # Правая вертикаль:
        for j_2 in range(i + 1, n - i):
            matrix[j_2][-i - 1] = c
            c += 1

        # Нижняя горизонталь:
        for j_3 in range(i + 1, m - i):
            matrix[-i - 1][-j_3 - 1] = c
            c += 1

        # Левая вертикаль:
        for j_4 in range(i + 1, n - (i + 1)):
            matrix[-j_4 - 1][i] = c
            c += 1

        c_1 += 2

# Вывод матрицы:
for i_2 in range(n):
    print(*matrix[i_2])
