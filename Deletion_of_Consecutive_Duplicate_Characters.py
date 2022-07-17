n=int(input())
for m in range(n):
    b=input()
    c=0
    for i in range(len(b)-1):
        x=b[i]
        y=b[i+1]
        if(x==y):
            c+=1
    print(c)