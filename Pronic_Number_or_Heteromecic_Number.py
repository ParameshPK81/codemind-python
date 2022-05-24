n=int(input())
for i in range(1,n+1):
        if n==i*(i+1):
            print('YES')
            break
else:
    print('NO')