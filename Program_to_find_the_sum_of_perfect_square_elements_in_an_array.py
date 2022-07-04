a=[1,4,9,16,25,36,49,64,81,100]
n=int(input())
b=list(map(int,input().split()))
sum=0
for i in b:
    if i in a:
        sum+=i
print(sum)