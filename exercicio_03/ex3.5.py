def mediaValor(notas):
    totalSoma = sum(notas)
    return totalSoma / len(notas)

def verificar(notas, recuperacao):
    
    positivo = all([n >= 0 for n in notas])
    mensagem = ''
    
    if not positivo:
        return [notas, recuperacao, "Nota(s) fora do intervalo"]
        
    media = mediaValor(notas)
    notaPassar = 5 if recuperacao else 7
    
    if not recuperacao:
        mensagem += f"Media: {media:.1f}\n"
    
    if media >= notaPassar:
        return [media, recuperacao, mensagem + "Aluno aprovado."]
    elif media < 5:
        return [media, recuperacao, mensagem + "Aluno reprovado."]
    else:
        recuperacao = True
        return [media, recuperacao, mensagem + "Aluno em exame."]

def verificarEntrada(notas):
    recuperacao = False
        
    media, recuperacao, mensagem = verificar(notas, recuperacao)
    print(mensagem)
    
    if recuperacao:
        notaRecuperacao = float(input("Nota do Exame: "))
        notasRecuperacao = [media,notaRecuperacao]
        mediaRecuperacao, recuperacao, mensagem = verificar(notasRecuperacao, recuperacao)
        print(mensagem)
        print (f"Media final: {mediaRecuperacao:.1f}")          
         
def entrada():
    notas = list(map(float, input().split()))
    verificarEntrada(notas)
 
if __name__ == "__main__":   
    entrada()