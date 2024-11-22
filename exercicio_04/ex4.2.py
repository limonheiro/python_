with open('entrada.txt', 'r') as f:
    number = int(f.readline())
    maxNumber = number
    pos = 1
    posMax = 1
    
    while number:
        number = int(number)
        if number > maxNumber:
            posMax = pos
            maxNumber = number
        number = f.readline()
        pos +=1
        
    print(maxNumber, posMax, sep='\n')
        