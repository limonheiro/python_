def intervalo():
    Number = float(input("Digite um número(pode ser número flutuante): "))
    
    if 0 > Number or Number > 100:
        return "Fora de intervalo"
    
    if Number <=25:
        return "Intervalo [0,25]"
    elif 25 < Number <= 50:
        return "Intervalo (25,50]"
    elif 50 < Number <= 75:
        return "Intervalo (50, 75]"
    
    return "Intervalo (75, 100]"

if __name__ == "__main__":
    print(intervalo())