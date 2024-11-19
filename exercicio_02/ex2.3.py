def bonus():
    Nome = input("nome: ")
    Salario = float(input("salario: "))
    Vendas = float(input("vendas: "))
    
    Total = Salario + Vendas*0.15
    
    print(f'TOTAL = {Total}')
    
if __name__ == "__main__":
    bonus()