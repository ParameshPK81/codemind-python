def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return 0
    else:
        return 1
    
n=int(input())
gd=0
ld=0
if prime(n):
    print(0)
else:
    for i in range(n,1000):
        if prime(i):
            gd=i-n
            break
    for i in range(n,1,-1):
        if prime(i):
            ld=n-i
            break
    if gd>ld:
        print(ld)
    elif gd<ld:
        print(gd)
    else:
        print(gd)