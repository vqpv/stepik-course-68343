nums = [i for i in range(int(input()), int(input()) + 1) if '0' not in str(i)]

for i in nums:
    if all(i % int(s) == 0 for s in str(i)):
        print(i, end=" ")
