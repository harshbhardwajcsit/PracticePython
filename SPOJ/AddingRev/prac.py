
test=input()
i=0
while i!=test:
   n1,n2=input().split()   ##taking inputs in single line


   # reverse and remove trailing zero
   nn= str(n1.rstrip('0'))[::-1]    ## str(ANY_number.rstrip('0'))        removing the trailing zero's and converting to string
   np = str(n2.rstrip('0'))[::-1]   ## str(ANY_number.rstrip('0'))[::-1]  reversing the string





   p=str(int(nn) + int(np))        ## type casting    ...interger to string
   print(str(p.rstrip('0'))[::-1])

i+=1