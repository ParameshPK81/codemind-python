n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    if(i%2==0):
        break
    else:
        sum+=i
print(sum)