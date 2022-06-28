def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
d=a+b
c=d+1
while True:
    if prime(c):
        break
    c+=1
print(c-d)