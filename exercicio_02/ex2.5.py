

def pontosQuadratico(x1, x2):
    return (x2 - x1) ** 2

def distanciaPontos(pontos):
    distancia = 0
    print(pontos)
    try:
        if len(pontos) != 2:
            return Exception
        else:
            x = []
            y = []
            for x1, x2 in pontos:
                x.append(x1)
                y.append(x2)
                
            for p1, p2 in [x, y]:
                distancia += pontosQuadratico(float(p1), float(p2))
    except:
        return print("Erro ao calcular a distância entre os pontos.")
    
    return distancia**(1/2)


def valores(size=2):
    pontos = [input().split() for _ in range(2)]
    distancia = distanciaPontos(pontos)
    print(f'{distancia:.4f}')

if __name__ == "__main__":
    valores()
