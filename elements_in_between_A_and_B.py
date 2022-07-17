n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=[]
sum=0
for i in a:
    if(i>=x and i<=y):
        b.append(i)
if(len(b)>0):
    print(*b)
else:
    print("-1")