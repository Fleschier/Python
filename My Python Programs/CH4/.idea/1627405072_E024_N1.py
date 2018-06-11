n=eval(input('请输入一个整型数：'))
from math import *                              #调用math函数

for i in range(2,n):                             #因为不用考虑1，所以从2开始循环
    if i ==2:                                    #为了方便直接单独讨论2
        print(i,end='\t')

    m=ceil(sqrt(i))

    for j in range(2,m+1):                       #验证是否为素数
        if i%j==0:
            break

    else:print(i,end='\t')                       #输出所有的素数
