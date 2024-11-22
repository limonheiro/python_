
def calculoAnos(dias):
    plural = lambda x, y: y if x>1 else ''
    
    anos = dias // 365
    meses = dias % 365 // 30
    dias = dias % 365 % 30
    
    return f'{anos} ano{plural(anos,'s')}\n{meses} mes{plural(meses,'es')}\n{dias} dia{plural(dias,'s')}'  


def entradaDias():
    dias = int(input())
    print(calculoAnos(dias))

entradaDias()