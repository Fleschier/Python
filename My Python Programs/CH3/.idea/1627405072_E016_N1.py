x=eval(input('输入一个小于五位的正整数：'))
if x//10000>=10:            #排除超过五位的数据
    print('数据非法')
elif x//10000>=1:          #讨论五位数的情况
    print('x为五位数')
    b1=x//10000
    c1=x//1000%10
    d1=x//100%10
    e1=x//10%10
    f1=x%10
    print('万位为：',b1,'\0千位为：',c1,'\0百位为：',d1,'\0十位为：',e1,'\0个位为：',f1)
    x1=f1*10000+e1*1000+d1*100+c1*10+b1
    print('x的逆序数为：',x1)
elif x//1000>=1:            #讨论四位数的情况
    print('x为四位数')
    c2=x//1000
    d2=x//100%10
    e2=x//10%10
    f2=x%10
    print( '千位为：', c2, '\0百位为：', d2, '\0十位为：', e2, '\0个位为：', f2)
    x2=f2*1000+e2*100+d2*10+c2
    print('x的逆序数为：', x2)
elif x//100>=1:             #讨论三位数的情况
    print('x为三位数')
    d3=x//100
    e3=x//10%10
    f3=x%10
    print(  '百位为：', d3, '\0十位为：', e3, '\0个位为：', f3)
    x3=f3*100+e3*10+d3
    print('x的逆序数为：', x3)
elif x//10>=1:              #讨论两位数的情况
    print('x为两位数')
    e4=x//10
    f4=x%10
    print( '十位为：', e4, '\0个位为：', f4)
    x4=f4*10+e4
    print('x的逆序数为：', x4)
else:                       #讨论一位数的情况
    print('x为一位数')
    print('个位为：',x)
    print('x的逆序数为：', x)