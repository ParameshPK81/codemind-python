n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n):
    if a[i]%2==0:
        if a[i-1]%2!=0:
            if a[i+1]!=0:
                c+=1
print(c)