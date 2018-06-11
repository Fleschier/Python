from random import *
a=int(uniform(100,999))
b=a%10*100+a%100-a%10+a//100
print('a=',a)
print('b=',b)