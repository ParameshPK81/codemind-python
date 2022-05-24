n=int(input())
max=n%10
while(n>0):
    d=n%10
    if(d>max):
        max=d
    n//=10
print(max)    