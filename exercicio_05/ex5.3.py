def fatorial(n):
    sum = 1
    
    
    if 0 > n or n > 13:
        return "Fora do intervalo permitido."
    
    for n in range(1, n+1):
        sum *= n
    
    return sum

n = int(input())
print(fatorial(n))