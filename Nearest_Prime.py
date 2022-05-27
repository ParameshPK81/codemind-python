def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return 0
    else:
        return 1
def near(a):
    l=f=dl=df=0
    for i in range(a,0,-1):
        if prime(i):
            f=i
            df=a-i
            break
    for i in range(a,10000):
        if prime(i):
            l=i
            dl=i-a
            break
    if df==dl:
        return f
    elif df>dl:
        return l
    elif dl>df:
        return f
n=int(input())
for i in range(n):
    a=int(input())
    print(near(a))