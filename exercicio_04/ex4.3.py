def somaImpar(x,y):
    sum=0
    minValue= min(x,y)
    maxValue = max(x,y)
    
    for i in range(minValue,maxValue):
        if i%2 == 1:
            sum += i
    return sum

def escreverPontos(n):
    entreImpares = []
    for _ in range(n):
        x, y = map(int, input().split())    
        entreImpares.append(somaImpar(x,y))        
    
    for i in entreImpares:
        print (i)

if __name__ == "__main__":
    number = int(input())
    escreverPontos(number)