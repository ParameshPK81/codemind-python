n=int(input())
a=list(map(int,input().split()))
t=int(input())
for i in range(0,n):
    if t==a[i]:
        print(i)
        break
else:
    print(-1)