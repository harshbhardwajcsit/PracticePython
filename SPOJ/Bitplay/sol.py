def getsum(num):
    sumi = 0
    num = str(num)
    i = 0
    while i < len(num):
        sumi += int(num[i])
        i += 1

    return sumi

test = int(input())
for j in range(0, test):

    n, k = input().split()
    n = int(n)
    k = int(k)
    j = n - 1
    list = []
    while j >= 0:
        if getsum("{0:b}".format(j)) <= k and j % 2 != 0:
            list.append(j)

        j -= 1
    list.sort()
    print(list[len(list)-1])

