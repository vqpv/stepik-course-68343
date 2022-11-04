lst_good_std = []

for _ in range(int(input())):
    student, grade = input().split()
    print(student, grade)
    if int(grade) >= 4:
        lst_good_std.append((student, grade))

print()
for good_std in lst_good_std:
    print(*good_std)
