test = input()
k = 0
while k < int(test):
    key = input()
    emsg = input()
    i = 1

    test = 10000
    while i < test:
        if len(key) * i >= len(emsg):
            break
        else:
            i = i + 1
    n = i

    i = 1
    m = key[::-1]
    while i < n:
        key = key + m
        m = m[::-1]
        i = i + 1
    ##print(key)
    i = 0
    list = []


    def defaultArg(i):
        num = ord(emsg[i])
        q = int(key[i])

        if num - q < 97:
            p = num - 97
            # print(chr(123 - (q - p)))
            list.append(chr(123 - (q - p)))

        else:
            # print(chr(num - q))
            list.append(chr(num - q))


    while i < len(emsg):
        defaultArg(i)
        i += 1

    print("".join(list))

k += 1
