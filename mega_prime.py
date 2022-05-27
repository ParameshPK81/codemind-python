def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n=int(input())
if(prime(n)):
    flag=0
    while n>0:
        rem=n%10
        if prime(rem):
            flag=1
            n//=10
        else:
            flag=0
            break
    if flag==1:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
        print("Not Mega Prime")