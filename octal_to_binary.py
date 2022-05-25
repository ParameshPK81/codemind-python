a=input()
j=0
for i in a:
    if i=='0':
        print("000",end='')
    elif i=='1':        
        if j>0:
            print('001',end='')
        else:
            print('1',end='')
    elif i=='2':
        if j>0:
            print('010',end='')
        else:
            print('10',end='')
    elif i=='3'            :
        if j>0:
            print('011',end='')
        else:
            print('11',end='')
    elif i=='4':
        print('100',end='')
    elif i=='5':
        print('101',end='')
    elif i=='6':
        print('110',end='')
    elif i=='7':
        print('111',end='')
    j+=1   