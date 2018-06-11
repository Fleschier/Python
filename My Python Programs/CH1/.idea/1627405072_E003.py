h=int(input('桶深h='))
r=int(input('底面半径r='))
from math import *
x=h*pi*r**2
print('需要的桶数=',int(2e4/x))