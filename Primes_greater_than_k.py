def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
x=int(input())
c=0
for i in a:
    if i==1:
        continue
    if(isprime(i)):
        if(i>=x):
            c+=1
print(c)