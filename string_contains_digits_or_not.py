n=int(input())
for k in range(n):
    a=input()
    for i in a:
        if(i.isdigit()):
            print("Yes")
            break
    else:
        print("No")