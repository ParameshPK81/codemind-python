x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in a:
    if i in b:
        c.append(i)
for j in c:
    if j not in d:
        d.append(j)
print(*d)