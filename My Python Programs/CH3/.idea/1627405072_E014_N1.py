x1,y1=eval(input('输入x1,y1:'))
x2,y2=eval(input('输入x2,y2:'))
x3,y3=eval(input('输入x3,y3:'))  #输入三个点坐标
from math import *
a=sqrt((x1-x2)**2+(y1-y2)**2)
b=sqrt((x1-x3)**2+(y1-y3)**2)
c=sqrt((x2-x3)**2+(y2-y3)**2)   #求出三角形三条边
if a+b<=c:
    print('数据错误')
elif a+c<=b:
    print('数据错误')
elif b+c<=a:
    print('数据错误')
elif fabs(a-c)>=b:
    print('数据错误')
elif fabs(b-c)>=a:
    print('数据错误')
elif fabs(a-b)>=c:
    print('数据错误')     #排除三条边不能构成三角形的情况
else:
    s=(a+b+c)/2
    area=sqrt(s*(s-a)*(s-b)*(s-c))  #求出三角形面积
    round=a+b+c                     #求出三角形周长
    print('三角形面积为：',area,'三角形周长为：',round)
