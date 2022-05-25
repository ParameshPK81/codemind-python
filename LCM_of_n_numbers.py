def lcm(a,b):
    l=max(a,b)
    while True:
        if l%a==0 and l%b==0:
            break
        else:
            l+=max(a,b)
    return l            
n=int(input())
arr=list(map(int,input().split()))
l=lcm(arr[0],arr[1])
for i in range(2,n):
    l=lcm(l,arr[i])
print(l)    
    