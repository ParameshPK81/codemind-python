def cd(n):
    c=0
    while(n):
        d=n%10
        c+=1
        n//=10
    return c
n=int(input())
a=list(map(int,input().split()))
m=min(a)
c=0
k=cd(m)
for i in range(len(a)):
    if k==cd(a[i]):
        c+=1
print(c)