n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    x=a.count(i)
    if x==i:
        if i not in b:
            b.append(i)
if(len(b)>0):
    print(*b)
else:
    print("-1")