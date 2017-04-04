key=input()
emsg=input()
i=1

test=10000
while i<test:
    if len(key)*i>=len(emsg):
        break
    else:
        i=i+1
n=i

i=1
m=key[::-1]
while i<n:
    key=key+m
    m=m[::-1]
    i = i + 1
##print(key)
i=0

while i<len(emsg):
    num=ord(emsg[i])
    q=int(key[i])
    if num-q<97:
        p=num-97
        print(chr(123-(q-p)))


else:
    print(chr(num-q))

    i = i + 1


