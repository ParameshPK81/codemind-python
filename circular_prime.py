def fun(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
rem=0
if fun(n):
    while(n):
        d=n%10
        n=n//10
        rem=rem*10+d
    if fun(rem):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')