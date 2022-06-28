def ad(n):
    s=0;c=0
    while(n>0):
        d=n%10
        s=s+d
        n//=10
    if s<10:
        return s
    else:
        n=s
        s=0
        return ad(n)
n=int(input())
print(ad(n))
    