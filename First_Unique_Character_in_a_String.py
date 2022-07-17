s=input()
for i in s:
    x=s.count(i)
    if(x==1):
        y=s.index(i)
        print(y)
        break
else:
    print("-1")