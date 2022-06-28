def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if i!=1 and prime(i):
        print(i)
    