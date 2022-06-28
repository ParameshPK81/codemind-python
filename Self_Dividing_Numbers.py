def sd(n):
    t=n
    c=0
    fc=0
    while(t>0):
        d=t%10
        if d!=0 and n%d==0:
            c+=1
        fc+=1
        t//=10
    if c==fc:
        return True
    else:
        return False
            
a=int(input());b=int(input())
for i in range(a,b+1):
    if(sd(i)):
        print(i,end=' ')