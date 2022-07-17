def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]==1:
        continue
    if isprime(a[i]):
        c+=1
print(c)        