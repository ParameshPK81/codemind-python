n=int(input())
a=list(map(int,input().split()))
x,y=0,0
for i in a:
    if i%2:
        y+=1
    else:
        x+=1
print(x,y)