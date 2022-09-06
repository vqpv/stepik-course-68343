n_1 = int(input())
nums = [int(input()) for _ in range(n_1)]
n_2 = int(input())

answer = 'НЕТ'

for i_1, j_1 in enumerate(nums):
    for i_2, j_2 in enumerate(nums):
        if j_1 * j_2 == n_2 and i_1 != i_2:
            answer = "ДА"
            break

print(answer)
