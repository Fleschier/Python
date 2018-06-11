x1,y1=eval(input('输入x1,y1:'))
x2,y2=eval(input('输入x2,y2:'))
x3,y3=eval(input('输入x3,y3:'))
from math import sqrt
a=sqrt((x1-x2)**2+(y1-y2)**2)
b=sqrt((x1-x3)**2+(y1-y3)**2)
c=sqrt((x2-x3)**2+(y2-y3)**2)
s=(a+b+c)/2
area=sqrt(s*(s-a)*(s-b)*(s-c))
print('{0:<7.2f}'.format(area))