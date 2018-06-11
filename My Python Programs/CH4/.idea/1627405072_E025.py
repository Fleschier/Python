a=eval(input('输入a：'))
n=eval(input('输入n：'))                                   #输入n和a

sum=0
x=0                                                         #预设两个变量以便下面储存值

while n>0:
    x=1+10*x                                                #相当于先计算a=1的情况
    sum=sum+x                                               #利用循环累加得到相当于（Sn/a）的值
    n-=1

sum=a*sum                                                   #最后再呈上a即可得到Sn
print('Sn=a+aa+...+aa..a={0}'.format(sum))
