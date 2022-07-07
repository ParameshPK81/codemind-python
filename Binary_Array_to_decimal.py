n=int(input())
a=list(map(int,input().split()))
num=0
for i in range(len(a)):
    num+=a[i]*pow(2,n-1)
    n-=1
print(num)