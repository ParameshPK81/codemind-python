def pal(n):
    r=0
    c=n
    while(n>0):
        d=n%10
        r=r*10+d
        n//=10
    if c==r:
        return True
    else:
        return False
a=int(input())
if pal(a):
    print(True)
else:
    print(False)