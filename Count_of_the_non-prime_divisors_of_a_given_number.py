def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
for i in range(n+1):
    if prime(i):
        continue
    if n%i==0:
        c+=1
print(c+1)