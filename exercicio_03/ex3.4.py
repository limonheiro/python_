def verificar(numeros):
    if len(numeros)!= 4:
        return "Valores nao aceito"
    condicoes =[
        numeros[1] > numeros[2] and numeros[3] > numeros[0],
        (numeros[2] + numeros[3]) > (numeros[0] + numeros[1]),
        numeros[2] >= 0 and numeros[3] >= 0,
        numeros[0] % 2 == 0
    ]
    if all(condicoes) :
        return  "Valores aceitos"
    else:
        return "Valores nao aceito"

def entradaValores():
    numeros = [ int(n) for n in input('').split()]
    print(verificar(numeros))
    
entradaValores()