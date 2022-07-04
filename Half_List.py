n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)-1,len(a)//2-1,-1):
    b.append(a[i])
for i in range(0,len(a)//2):
    b.append(a[i])
print(*b)