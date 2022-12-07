m, n = int(input()), int(input())
s_1 = {input() for i in range(n)}

if m > 1:
    for _ in range(m - 1):
        j = int(input())
        s_1 &= {input() for i in range(j)}
    
print(*sorted(s_1), sep='\n')
