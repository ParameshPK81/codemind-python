n=int(input())
fs=[]
a=0;b=1;c=0
for i in range(1000):
    fs.append(c)
    c=a+b
    a=b;b=c
if n in fs:
    print(True)
else:
    print(False)
    