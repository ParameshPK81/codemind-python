s=input().lower()
s1=(s.split(' '))[0]
b=[]
for i in s1:
    a=0
    for j in s.split(' '):
        if i in j:
            a+=1
        else:
            a=0
    if a==len(s.split(' ')):
        b.append(i)
print(len(b))