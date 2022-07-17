n=int(input())
for k in range(n):
    a=input()
    x=a[::-1]
    if(x==a):
        if(len(a)%2==0):
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")