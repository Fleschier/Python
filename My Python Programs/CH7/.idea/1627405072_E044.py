from random import uniform

a=set()
b=set()
i=0
while i<=200:
    a.add(int(uniform(0,500)))
    b.add(int(uniform(0,500)))
    i+=1                                #通过随机数生成两个200个数的集合

print('两集和不同的数据为：')
count=0
differ=a.symmetric_difference(b)        #调用函数求得对称差集并格式化输出
for i in differ:
    print('{:5d}'.format(i),end=' ')
    count+=1
    if count%10==0:
        print()
print()

print('两集和相同的数据为：')
count=0
same=a.intersection(b)                  #调用函数求得交集，并格式化输出
for i in same:
    print('{:5d}'.format(i),end='')
    count+=1
    if count%10==0:
        print()
print()