def mediaValor(notas):
    totalSoma = sum(notas)
    return totalSoma / len(notas)

def verificar(notas, recuperacao):
    
    positivo = all([n >= 0 for n in notas])
    
    if not positivo:
        return [notas, recuperacao, "Nota(s) fora do intervalo"]
        
    notas = mediaValor(notas)
    notaPassar = 5 if recuperacao else 7
    
    if not recuperacao:
        print(f"Media: {notas:.1f}")
    
    if notas >= notaPassar:
        return [notas, recuperacao, "Aluno aprovado."]
    elif notas < 5:
        return [notas, recuperacao,"Aluno reprovado."]
    else:
        recuperacao = True
        return [notas, recuperacao,"Aluno em exame."]
          
def entrada():
    recuperacao = False
    valores = list(map(float, input().split()))
    media, recuperacao, mensagem = verificar(valores, recuperacao)
    
    print(mensagem)
    
    if recuperacao:
        notaRecuperacao = float(input("Nota do Exame: "))
        notasRecuperacao = [media,notaRecuperacao]
        mediaRecuperacao, recuperacao, mensagem = verificar(notasRecuperacao, recuperacao)
        print(mensagem)
        print (f"Media final: {mediaRecuperacao:.1f}")      
 
if __name__ == "__main__":   
    entrada()