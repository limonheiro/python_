def menu(code:int, quant:int):
    menu = {
        1: {"especificacao": "Cachorro Quente", "preco": 4.00},
        2: {"especificacao": "X-Salada", "preco": 4.50},
        3: {"especificacao": "X-Bacon", "preco": 5.00},
        4: {"especificacao": "Torrada Simples", "preco": 2.00},
        5: {"especificacao": "Refrigerante", "preco": 1.50},
    }
    try:
        if quant > 0:
            return menu[code]['preco'] * quant
        else:
            return 'Quantidade fora do intervalo permitido.'
    except:
        return "Erro ao calcular o valor"
    
def caixa():
    try:
        code, quant = input("Digite o codigo e quantidade sepado por espaço: ").split()
        Total = menu(int(code), int(quant))
        print(f'Total: R$ {Total}')
    except:
        print("erro")
    
if __name__ == "__main__":
    caixa()