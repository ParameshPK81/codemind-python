n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i !=0:
        b.append(i)
    else:
        c+=1
for j in range(c):
    b.append(0)
print(*b)