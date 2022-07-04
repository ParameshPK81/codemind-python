n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(n):
    for j in range(m):
        if(i==j):
            c.insert(b[j],a[i])
print(*c)