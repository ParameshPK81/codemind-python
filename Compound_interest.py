p,r,t=map(int,input().split())
c=r/100
k=1+c
po=k**t
ci=p*po
print("{0:.2f}".format(ci))