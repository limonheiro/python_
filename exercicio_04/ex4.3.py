def somaImpar(x):
    sum=0
    x.sort()
    minValue, maxValue = x
    
    for i in range(minValue,maxValue):
        if i%2 == 1:
            sum += i
    return sum

def escreverPontos(n):
    entreImpares = []
    for _ in range(n):
        x = list(map(int, input().split()))    
        entreImpares.append(somaImpar(x))        
    
    for i in entreImpares:
        print (i)

if __name__ == "__main__":
    number = int(input())
    escreverPontos(number)