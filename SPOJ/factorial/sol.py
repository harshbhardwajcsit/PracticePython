test = int(input())
for i in range(0,test):
    n = int(input())
    fac = 1
    while n > 0:
        fac *= n
        n -= 1

    print(fac)




