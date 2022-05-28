def add(n):
    s=0
    d=n
    while True:
        s=0
        while d>0:
            r=d%10
            s+=r
            d//=10
        if s<10:
            return s
        else:
            d=s
            s=0
            continue
a=int(input())
res=add(a)
print(res)