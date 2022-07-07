def prime(n):
    for i in range(2,((int(n**0.5))+1)):
        if n%i==0:
            return False
    else:
        return True
def palindrome(n):
    n=str(n)
    k=n[::-1]
    if k==n:
        return True
    else:
        return False
n=int(input())
# for i in range(n+1,10000):
#     if prime(i):
#         if palindrome(i):
#             print(i)
#             break
i = n+1
while(True):
    if prime(i) and palindrome(i):
        print(i)
        break
    i = i+1    