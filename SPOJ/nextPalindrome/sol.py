test = int(input())
for i in range(0,test):
    n = int(input())
    k=n+1
    while k < 1000000 :
        c=k
        st=str(c)
        if st == st[::-1]:
            break

        k += 1

    print(st)




