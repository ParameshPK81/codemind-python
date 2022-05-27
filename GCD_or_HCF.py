def gcd(a,b):
    if a>b:
        a,b=b,a
    c=a
    while True:
        if a%c==0 and b%c==0:
            return c
        c-=1

n,m=map(int,input().split())
print(gcd(n,m))