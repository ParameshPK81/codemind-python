n=int(input())
A=list(map(int,input().split()))
res = max(set(A), key =A.count)
print(res)