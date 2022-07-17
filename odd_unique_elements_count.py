n=int(input())
a=list(map(int,input().split()))
a=set(a)
c=0
for i in a:
    if(i%2==1):
        c+=1
print(c)