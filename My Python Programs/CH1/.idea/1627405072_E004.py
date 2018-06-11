print('坐标A=（a,b)\n坐标B=（c,d）')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))
tuple1=a,b
tuple2=c,d
print('点A',tuple1,'\n点B',tuple2)
from math import *
x=(a-c)**2
y=(b-d)**2
print('A,B两点间的距离=',sqrt(x+y))