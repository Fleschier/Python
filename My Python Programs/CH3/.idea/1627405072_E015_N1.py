x1,y1=eval(input('输入x1,y1:'))
r=eval(input('输入半径r:'))
x2,y2=eval(input('输入x2,y2:'))   #输入待判断点坐标
from math import *
a=sqrt((x1-x2)**2+(y1-y2**2))      #算出点到圆心的距离
if a<=r:
    print('点（x2,y2）在圆内')
else:
    print('点（x2,y2）在圆外')
