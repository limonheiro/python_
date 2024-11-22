def verificaQuadrante(x,y):
    quadrantes = {
        (x>0, y>0) : 'primeiro',
        (x<0, y>0) : 'segundo',
        (x<0, y<0) : 'terceiro',
        (x>0, y<0) : 'quarto'
    }
    if not 0 in [x,y]:
        for k,v in quadrantes.items():
            if all(k):
                print(v)
                return True
    return False

def entradaPontos():
    x, y = map(int, input().split())
    
    while verificaQuadrante(x,y):
        x, y = map(int, input().split())

entradaPontos()