
def calculadora(code, quant, price):
    if price > 0 and quant > 0:
        return quant * price
    else:
        return Exception    
        

def valores(sizeInput=2):
    Valor = 0
    Entrada = [input().split() for _ in range(sizeInput)]

    for code, quant, price in Entrada:
        try:
            Valor += calculadora(code, int(quant), float(price))
        except Exception:
            print (f"Valor(es) de quantidade ou preço incorreto.") 
            return 0
        
    print(f'VALOR A PAGAR: R$ {Valor:.2f}')
    
if __name__ == "__main__":
    valores()