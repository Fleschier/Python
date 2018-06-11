l=l=[65.5,70.2,100.5,45.5,88.8,55.5,73.5,67.8]

a=sum(l)/8                          #求出平均值a

count=0
for i in l:
    i=(i-a)**2
    l[count]=i
    count=count+1                   #将列表中每个元素处理为差的平方的形式

def f(x,y):
    return x+y                      #定义函数

import functools

d=functools.reduce(f,l)              #相当于求出方差的8倍

print('这组数据的方差为：',d/8)       #输出最后的方差的值