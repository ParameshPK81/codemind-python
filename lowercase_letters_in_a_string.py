s=input()
c=0
for i in s:
    if ord(i)>=96 and ord(i)<=122:
        c+=1
print(c)