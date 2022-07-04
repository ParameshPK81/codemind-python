a=int(input())
b=int(input())
sum=0
for i in range(a):
    arr=list(map(int,input().split()))
    for j in arr:
        sum+=j
print(sum)