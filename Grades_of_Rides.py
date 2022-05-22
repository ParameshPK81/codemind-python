h,sp,s=map(int,input().split())
if h>=50 and sp>=60 and s>=100:
    print(10)
elif h>=50 and sp>=60 and s<=100:
    print(9)
elif h<=50 and sp>=60 and s>=100:
    print(8)
elif h>=50 and sp<=60 and s>=100:
    print(7)    
elif h<=50 and sp<=60 and s<=100:
    print(5)
else:
    print(6)