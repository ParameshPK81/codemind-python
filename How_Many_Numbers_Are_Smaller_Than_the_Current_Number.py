n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]>a[j]:
            c+=1
    b.append(c)
print(*b)