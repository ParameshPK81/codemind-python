n=int(input())
sq=n*n
sum=0
while (sq>0) :
    d=sq%10
    sum=sum+d
    sq=sq//10
if sum==n:
    print('Neon Number')
else :
    print('Not Neon Number')