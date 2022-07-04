
n=int(input())
a=list(map(int,input().split()))
t=int(input())
first = -1
last = -1
for i in range(0,len(a)) :
    if (t != a[i]) :
        continue
    if (first == -1) :
        first = i
    last = i
print(first,last)