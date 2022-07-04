n=int(input())
a=list(map(int,input().split()))
x=1
b=[]
for i in a:
    x=x*i
for i in a:
    b.append(x//i)
print(*b)