def dc(n):
    c=0
    while(n):
        d=n%10
        c+=1
        n//=10
    return c
n=int(input())
a=list(map(int,input().split()))
c=0
k=(max(a))
l=dc(k)
for i in range(len(a)):
    if l==dc(a[i]):
        c+=1
print(c)