n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
d=0
for i in a:
    if(i>k):
        c+=1
    else:
        d+=1
    if(c==2):
        break
print(d)    