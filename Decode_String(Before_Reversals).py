t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    s=input()
    while b>0:
        fs=s[:b]
        fs=fs[::-1]
        s=fs+s[b:]
        b-=1
    print(s)