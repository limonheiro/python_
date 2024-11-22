def verificarDivisao(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 'divisao impossivel'

def valores(n):
    saida = []
    for _ in range(n):
        x,y = map(int, input().split())
        saida.append(verificarDivisao(x,y))
    
    for i in saida:
        print(i)

if __name__ == "__main__":
    vezes = int(input())
    valores(vezes)