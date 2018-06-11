from time import *
s=time()
m=0
h=0
d=0
m=s//60
while m//60>=1:
    h=h+1
    m=m-60
    while h//24>=1:
            d=d+1
            h=h-24
print('现在距离1970年1月1日',d,'天',h,'小时')