with open('numeros.txt','r') as f:
    numeros = f.readlines()
    numeros = list(map(int, numeros))
    
    print(f'Soma: {sum(numeros)}')
    print(f'Média: {sum(numeros)/len(numeros)}')
    print(f'Menor: {min(numeros)}')
    print(f'Maior: {max(numeros)}')
    
