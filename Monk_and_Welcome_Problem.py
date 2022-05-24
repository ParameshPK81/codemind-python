n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for i in range(len(a)):
  res=a[i]+b[i]
  print(res,end=' ')    