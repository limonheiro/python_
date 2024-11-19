

def salario():
    Number = int(input("NUMBER: "))
    if Number > 100 :
        return print("Número do funcionario fora do padrão!")
    
    HourSalary = float(input("Valor por hora trabalha: "))
    
    if HourSalary < 10 :
        return print("Horas Trabalhadas fora do padrão!")
        
    HoursWork = int(input("Horas Trabalhada: "))
    Salary = HourSalary * HoursWork
    
    print(f"NUMBER = {Number:}\nSALARY = U$ {Salary:.2f}")
    
if __name__ == "__main__":
    salario()