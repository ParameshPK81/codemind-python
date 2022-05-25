def rev(n):
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n//=10
    return r    
def palindrome(k):
    c=k;r=0
    while(k>0):
        d=k%10
        r=r*10+d
        k//=10
    if r==c:
        return True
    else:
        return False
n=int(input())
k=n+rev(n)        
while(k>0):
    if(palindrome(k)):
        print(k)
        break
    else:
        k+=rev(k)
