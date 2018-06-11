a=0
x=1
while x<=5:
    a=(a+100)*(1+0.005)
    x=x+1
print('总金额：',format(a,'>0.5f'))
b=(a-500)/500
print('{0} {1:>0.2f}%'.format('收益率：',b*100))