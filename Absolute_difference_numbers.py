n,m=map(int,input().split())
n=str(n)
x=[i for i in n]
aa=x[:m]
bb=x[-m:]
xx=''
yy=''
for i in aa:
    xx+=i
for i in bb:
    yy+=i
print(abs(int(xx)-int(yy)))    