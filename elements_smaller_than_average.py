n=int(input())
a=list(map(int,input().split()))
sum=c=0
for i in a:
    sum+=i
avg=sum//n
for i in a:
    if(i<=avg):
        c+=1
print(c)