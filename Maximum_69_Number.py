n=int(input())
b=c=d=r=no=0
while(n>0):
    b=n%10
    n//=10
    r=r*10+b
while(r>0)    :
    c=r%10
    r=r//10
    if(d<1):
        if c==6:
            c=9
            d=1
    no=no*10+c                
print(no)    