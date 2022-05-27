import math
a=int(input())#9
arr=[]
for i in range(100):
    arr.append(math.pow(2,i))### 2 4 8 16 32 64 128 256 512 1024
f=l=df=dl=0
for i in range(100):
    if arr[i]>a:
        l=arr[i]
        f=arr[i-1]
        dl=l-a
        df=a-f
        print(int(min(dl,df)))
        break
