n=int(input())
a=list(map(int,input().split()))
o=0
e=0
for i in range(len(a)):
    if i%2:
        o+=a[i]
    else:
        e+=a[i]
if(e-o==0):
    print('YES')
else:
    print('NO')