a=input()
c=0
l=len(a)
for i in range(1,l-1):
    if ord(a[i])>64 and ord(a[i])<91:
        c+=1
print(c+1)