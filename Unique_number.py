def crd(n):
    c=[0]*10
    res=0
    while n>0:
        d=n%10
        c[d]+=1
        n=n//10
    for i in range(10) :
        if(c[i]>1):
            res+=1
    return res            
n=int(input())            
res=crd(n)
if res>0:
    print('Not Unique Number')
else:
    print('Unique Number')