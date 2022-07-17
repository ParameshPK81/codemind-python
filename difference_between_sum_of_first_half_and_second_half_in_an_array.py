n=int(input())
a=list(map(int,input().split()))
x=n//2
l=0
r=0
sum=0
for i in range(x):
    l=l+a[i]
for i in a:
    sum=sum+i
r=sum-l
print(abs(r-l))