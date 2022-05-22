n=int(input())
for i in range(n):
    a=int(input())
    c=0
    for j in range(1,a):
        if j**2==a:
            c=1
            break
    if c==1:
        print(True)
    else:
        print(False)