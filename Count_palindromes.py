def pal(n):
    n=str(n)
    if n==n[::-1]:
        return True
    return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if pal(i):
        c+=1
print(c)