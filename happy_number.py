def happy(a):
    su=0
    while(1):
        su=0
        while a>0:
            rem=a%10
            su+=rem**2
            a//=10
        if su<10:
            break
        else:
            a=su
            continue
    if su==1 or su==7:
        return 1
    else:
        return 0
a=int(input())
res=happy(a)
if res==1:
    print(True)
else:
    print(False)