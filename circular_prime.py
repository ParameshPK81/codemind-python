def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
r=0
if prime(n):
    while n>0:
        d=n%10
        n=n//10
        r=r*10+d
    if prime(r):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')