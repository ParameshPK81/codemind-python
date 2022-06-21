str = input()
sum = 0
for c in str:
    if c.isdigit() == True:
        sum += 1
if sum>0:
    print('Contains',sum,'digit')
else:
    print('Doesn't contain digit')