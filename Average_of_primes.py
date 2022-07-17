def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
sum=c=0
for i in a:
    if i==1:
        continue
    if(isprime(i)):
        c+=1
        sum=sum+i
x=sum/c
print("{:.2f}".format(x))

