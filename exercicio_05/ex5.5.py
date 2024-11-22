import math
def contarTempo(PA, PB, G1, G2):
    IA = PA
    IB = PB
    G1 /= 100
    G2 /= 100
    for n in range(102):
        PA += math.floor(PA*(G1))
        PB += math.floor(PB*(G2))
        
        if PA > PB:
            return f'{n+1} ano{"s" if n>1 else ""}'
        elif PA < PB and n>100:
            return "Mais de 1 seculo"

def escreverDados(n):
    mensagem = []
    for _ in range(n):
        PA, PB, G1, G2 = map(float, input().split())
        mensagem.append(contarTempo(PA,PB,G1,G2))
    
    return mensagem

n = int(input())
resultado = escreverDados(n)   
for m in resultado:
    print(m)
    