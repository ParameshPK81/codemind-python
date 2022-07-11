n=int(input())
a=list(map(int,input().split()))
c=k=0
for i in range(len(a)-1,-1,-1):
    if a[i]%2!=0:
        c+=1
    if i%2!=0:
        if a[i]%2!=0:
            k+=1
if c==k:
    print(True)
else:
    print(False)
    