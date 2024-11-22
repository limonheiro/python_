def media(notas):
    return sum(notas)/len(notas)

def verificarEntrada(nota):
    if nota < 0 or nota > 10:
        return 'nota invalida'
        
    return nota

def entrada():
    notas = []
    while len(notas) != 2:
        nota = float(input())
        saida = verificarEntrada(nota)
        if type(saida) is str:
            print(saida)            
        else:
            notas.append(saida)
            
    print(f'media = {media(notas):.2f}')
    
entrada()