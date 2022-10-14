letters = input().split()
n = int(input())

lst = [letters[i::n] for i in range(n)]

print(lst)
