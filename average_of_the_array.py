n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(len(a)):
    s+=a[i]
avg=s/len(a)
print("%.2f"%avg)