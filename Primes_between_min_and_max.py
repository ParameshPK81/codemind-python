def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
x=min(a)
y=max(a)
for i in range(n):
    if x==a[i]:
        a1=i
        break
for i in range(n-1,-1,-1):
    if y==a[i]:
        a2=i
        break
c=0
if a1>a2:
    a1,a2=a2,a1
for i in range(n):
    if(i>=a1 and i<=a2):
     if a[i]<=1:
         continue
     if isprime(a[i]):
            c+=1
print(c)