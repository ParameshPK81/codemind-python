n=int(input())
a=list(map(int,input().split()))
for i in range(0,n-1,2):
    y=a[i+1]
    for j in range(y):
        print(a[i],end=' ')
#print(*b)