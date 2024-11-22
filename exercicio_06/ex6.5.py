def sequecia(coll,number):
    for n in range(1,number+1):
        print(n, end=' ')
        if n % coll == 0:
            print()

def entrada():
    coll, number = map(int, input().split())
    sequecia(coll, number)
    
entrada()