n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
for i in a:
    if(a.count(i)==k):
        b.append(i)
b=set(b)
if(len(b)>0):
    print(*b)
else:
    print("-1")