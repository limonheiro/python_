def sequencia(n):
    for i in range(1,n+1):
        exp2 = i**2
        exp3 = i**3
        print(i, exp2, exp3)
        print(i, exp2+1, exp3+1)

n = int(input())
sequencia(n)
    