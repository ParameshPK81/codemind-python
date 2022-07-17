n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    x=a.count(i)
    if x==i:
        if i not in b:
            b.append(i)
y=len(b)
if(len(b)>0):
    sum=0
    for i in b:
        sum=sum+i
    sum=sum/y
    print("{:0.2f}".format(sum))
else:
    print("-1")