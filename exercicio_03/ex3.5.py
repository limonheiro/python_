def mediaValor(notas):
    totalSoma = sum(notas)
    return totalSoma / len(notas)

def verificar(notas, recuperacao):
    
    positivo = all([n >= 0 for n in notas])
    
    if not positivo:
        return [notas, recuperacao, "Nota(s) fora do intervalo"]
        
    media = mediaValor(notas)
    notaPassar = 5 if recuperacao else 7
    
    if not recuperacao:
        print(f"Media: {media:.1f}")
    
    if media >= notaPassar:
        return [media, recuperacao, "Aluno aprovado."]
    elif media < 5:
        return [media, recuperacao,"Aluno reprovado."]
    else:
        recuperacao = True
        return [media, recuperacao,"Aluno em exame."]
          
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