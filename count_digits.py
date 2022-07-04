'''def count(n):
    c=0
    if n<0 or n>0:
        n=abs(n)
        while n>=0:
            d=n%10
            n//=10
            c+=1
    if n==0:
        c=1
    return c
    '''
n=int(input())
a=list(map(int,input().split()))
for i in a:
    i=abs(i)
    i=str(i)
    print(len(i),end=" ")