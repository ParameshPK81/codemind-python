def fact(n):
    p=1
    for i in range(n,1,-1):
       p=p*i
    return p       
n=int(input())
s=0
k=n
while(n>0):
    d=n%10
    s=s+fact(d)
    n=n//10
if k==s:
    print('The number',k,'is a strong number')
else:
    print('The number',k,'is not a strong number')