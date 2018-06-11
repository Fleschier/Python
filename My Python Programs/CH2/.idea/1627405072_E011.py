from random import *
import cmath
from math import *
x=int(uniform(10,50))
y=int(uniform(10,50))
a=x+cmath.sqrt(-y**2)
print('复数a为','{0:>7f}'.format(a))
b=cmath.phase(a)
print('a的幅角为','{0:>7f}度'.format(b*180/pi))
c=sqrt(x**2+y**2)
print('a的模为','{0:>7f}'.format(c))