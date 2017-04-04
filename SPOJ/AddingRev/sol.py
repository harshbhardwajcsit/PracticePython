test=int(input())
for i in range(0,test):
   n1,n2=input().split()


   # reverse and remove trailing zero
   nn= str(n1.rstrip('0'))[::-1]
   np = str(n2.rstrip('0'))[::-1]
   p=str(int(nn) + int(np)).rstrip('0')

   print(p[::-1])
