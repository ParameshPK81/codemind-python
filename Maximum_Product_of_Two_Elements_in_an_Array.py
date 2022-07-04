a=list(map(int,input().split()))
k=max(a)
b=a.remove(k)
m=0
x=k-1
for i in range(0,len(a)):
    if(a[i]>m):
        m=a[i]
y=m-1
print(x*y)