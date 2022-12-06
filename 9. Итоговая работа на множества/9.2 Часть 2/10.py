m, n = int(input()), int(input())

s = set()

for _ in range(m + n):
    student = input()
    if student in s:
        s.remove(student)
    else:
        s.add(student)

print(len(s) if s else "NO")
