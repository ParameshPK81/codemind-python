n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
        c.append(a.count(i))
for i in range(len(b)):
    print(b[i],c[i],end=' ')