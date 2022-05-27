n=int(input())
if n>0:
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    print(r)
if n<0:
    n=-1*n
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    r=-1*r
    print(r)
    