n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    x=a.count(i)
    if(i==x):
        b.append(i)
b=set(b)
for i in b:
    c+=1
print(c)