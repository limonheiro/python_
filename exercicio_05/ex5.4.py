def calculoMedia(idades):
    return sum(idades)/len(idades)

def entradaIdades():
    idades = []
    n = int(input())
    
    while n > 0:
        idades.append(n)  
        n = int(input())

    media = calculoMedia(idades)
    print(media)
    
entradaIdades()