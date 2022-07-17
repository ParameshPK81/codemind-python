def pretty(n):
    if n%10==2 or n%10==3 or n%10==9:
        return True
    else:
        return False
n=int(input())
c=0
for i in range(n):
    c=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        if pretty(i):
            c+=1
    print(c)