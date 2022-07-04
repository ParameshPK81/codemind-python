t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    while n:
        b.append(max(a))
        a.remove(max(a))
        if len(a)==0:
            break
        b.append(min(a))
        a.remove(min(a))
        if(len(a)==0):
            break
        n-=1
    print(*b)
    t-=1