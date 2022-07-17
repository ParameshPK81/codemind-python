m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
c=[]
for i in a:
    if i in b:
        c.append(i)
for j in b:
    if j in a:
        c.append(j)
print(len(c)//2)