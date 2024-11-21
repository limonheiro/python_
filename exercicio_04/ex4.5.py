x,y = [int(input()) for _ in range(2)]
minN = min(x,y)
maxN = max(x,y)

for i in range(minN, maxN):
    if i%5 in [2,3]:
        print(i)