a=int(input())
arr=list(map(int,input().split()))
mi=arr[0]
j=1
while j<a:
    if arr[j]%mi==0:
        j+=1
    else:
        mi=arr[j]%mi
print(mi)