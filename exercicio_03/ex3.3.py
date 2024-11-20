def reajusteSalarial(salario):
    if salario < 0:
        return "Salário fora de intervalo!"
    
    if salario <= 400:
        return 0.15
    elif 400.01 <= salario <= 800:
        return 0.12
    elif 800.01 <= salario <= 1200:
        return 0.1
    elif 1200.01 <= salario <= 2000:
        return 0.07
    
    return 0.04

def novoSalario():
    salario = float(input("Salário: "))
    reajuste = reajusteSalarial(salario)
    ganho = salario * reajuste
    print(f"Novo salario: {(salario + (ganho)):.2f}\nReajuste ganho: {ganho:.2f}\nEm percentual: {(reajuste*100):.0f} %")

if __name__ == "__main__":
    novoSalario()