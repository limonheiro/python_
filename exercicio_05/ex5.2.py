def fibonacci(n):
    if not 0 < n < 46:
        return 0
    
    soma = 0
    anterior = 0
    listSequenc = [0]
    
    for n in range(n):
        
        if n <=2 :
            soma = 1
            anterior = 1
        else:    
            soma = anterior + soma
        
        listSequenc.append(soma)
    
    print(listSequenc)

if __name__ == "__main__":
    n = int(input())
    fibonacci(n)