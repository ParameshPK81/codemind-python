n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    sum+=i
k=sum//n
c=0
for i in a:
    if i>=k:
        c+=1
print(c)