n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(' ',end='')
    for k in range(1,i+1):
        print(chr(64+k),end='')
    for I in range(i-1,0,-1):
        print(chr(64+I),end='')
    print()    