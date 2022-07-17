n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=[]
sum=0
for i in a:
    if(i>=x and i<=y):
        b.append(i)
for i in b:
    sum+=i
print(sum)