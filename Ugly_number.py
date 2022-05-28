n=int(input())
f=0
if n>0:
    while n>0:
        if n%2==0:#6
            n//=2#3
        elif n%3==0:#3
            n//=3#1
        elif n%5==0:
            n//=5
        else:
            f=1
            break
if f==1:
    if n==1:
        print('Ugly Number')
    else:
        print('Not Ugly Number')
else:
    print('Not Ugly Number')