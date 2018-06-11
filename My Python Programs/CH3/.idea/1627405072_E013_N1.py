a=float(input('input a:'))
b=float(input('input b:'))
c=float(input('input c:'))      #输入三个浮点数
print('方程为：ax**2+bx+c=0')
k=b**2-4*a*c
if a==0:                #讨论a=0的情况
    x=-c/b
    print('方程解为',x,'\n此时a为0')
elif a!=0:          #讨论a不等于0的情况
    if k<0:         #讨论无实数解的情况
        from cmath import *
        x1=(-b+sqrt(k))/2*a
        x2=(-b-sqrt(k))/2*a
        print('{0},{1:10.5f},{2:10.5f},{3}'.format('方程解为：',x1,x2,'\n此时方程无实数解'))
    else:             #剩余的即为有两个实数解的情况
        from math import *
        x1=(-b+sqrt(k))/2*a
        x2=(-b+sqrt(k))/2*a
        print('方程解为：',x1,x2,'\n此时方程有实数解')


