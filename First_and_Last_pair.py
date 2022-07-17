n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
r=[]
if(n%2==0):
    for i in range(n//2):
        x=a[i]
        b.append(x)
    for j in range(n-1,n//2-1,-1):
        y=a[j]
        c.append(y)
    for m in range(len(b)):
        p=b[m]
        q=c[m]
        r.append(p)
        r.append(q)
    print(*r)
else:
    for i in range(n//2+1):
        x=a[i]
        b.append(x)
    for j in range(n-1,n//2,-1):
        y=a[j]
        c.append(y)
    c.append(0)
    for m in range(len(b)):
        p=b[m]
        q=c[m]
        r.append(p)
        r.append(q)
    print(*r)

