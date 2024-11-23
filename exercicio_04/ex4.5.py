try:
    lista = [int(input()) for _ in range(2)]
except (ValueError, NameError):
    print("Insira numero inteiro")
    
lista.sort()
minN,maxN = lista

for i in range(minN, maxN):
    if i%5 in [2,3]:
        print(i)