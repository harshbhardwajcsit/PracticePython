test = int(input())
for i in range(0, test):
    list1 = []
    d11, d12, d13, d14 = input().split()
    d21, d22, d23, d24 = input().split()
    list1.append(d11)
    list1.append(d12)
    list1.append(d13)
    list1.append(d14)
    ## print(list1)

    dict1 = {d21: d21, d22: d22, d23: d23, d24: d24}
    c = 0
    for i in list1:
        if dict1.has_key(i)==True:
            c += 1
    print(c)
