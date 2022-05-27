a=input()
b=str(a)
hh=b[0:2]
mm=b[3:5]
ha=int(hh)
ma=int(mm)
if(ha>12):
    ha=ha-12
hha=0.5*(ha*60+ma)    
mha=6*ma
angle=abs(hha-mha)
if angle>180:
    angle=abs(angle-360)
print(angle)    
