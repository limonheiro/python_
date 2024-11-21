def fibonacci(n):
    if n == 0:
        return 0
    
    return fibonacci(n-1)

n = int(input())
print(fibonacci(n))