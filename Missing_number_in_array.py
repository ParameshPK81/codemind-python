t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=(n*(n+1))//2
    print(x-sum(a))
    