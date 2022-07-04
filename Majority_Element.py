n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(a.count(i)) # 2 1
for i in a: #3 2 
    if a.count(i)==max(b):
        print(i)
        break