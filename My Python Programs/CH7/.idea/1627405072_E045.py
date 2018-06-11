from random import uniform
import re
p=re.compile('\d+')                                 #设置正则表达式，以便下面将输入的数据从字符串中取出来

a=set()
b=set()

def generator(x):                                   #定义generator()函数生成符合条件的集合x
    n=int(uniform(0,9))
    i=0
    while i<=n:
        x.add(int(uniform(0,1000)))
        i+=1

generator(a)                                        #用generator()函数生成集合a和b
generator(b)

def output(x):                                      #定义函数output()用来输出集合x中的元素
    count=0
    for i in x:
        print('{:5d} '.format(i),end='')
        count+=1
        if count%10==0:
            print()
    print()

print('集合A的数据为：')                           # 格式化输出集合中的数据
output(a)
print('集合B的数据为：')
output(b)

count=0
c=set()
rs1=input('请输入A|B的结果：')
rs1=p.findall(rs1)                                  #从输入的数据字符串中提取出数据并放入一个列表，与正确答案相比较来判断用户输入的答案是否正确，下面同理。
for i in rs1:
    c.add(int(i))

while a|b!=c:

    print('答案错误')
    rs1 = input('请重新输入A|B的结果：')
    rs1 = p.findall(rs1)
    for i in rs1:
        c.add(int(i))
    count+=1
    if count%2==0:
        print('正确结果为：',a|b)
        break
else:
    print('答案正确')

count = 0
c = set()
rs1 = input('请输入A&B的结果：')
rs1 = p.findall(rs1)
for i in rs1:
    c.add(int(i))

while a & b != c:
    print('答案错误')
    rs1 = input('请重新输入A&B的结果：')
    rs1 = p.findall(rs1)
    for i in rs1:
        c.add(int(i))
    count += 1
    if count % 2 == 0:
        print('正确结果为：', a & b)
        break
else:
    print('答案正确')