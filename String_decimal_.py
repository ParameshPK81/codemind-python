n=int(input())
for k in range(n):
    a=input()
    c=0
    for i in a:
        if(i.isdigit()):
            c+=1
    if(c==len(a)):
        print(True)
    else:
        print(False)