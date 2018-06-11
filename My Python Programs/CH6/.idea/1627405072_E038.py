from random import *

l=[[0]*4 for a in range(4)]
l1=[[0]*4 for a in range(4)]        #为了防止浅拷贝导致l1,l2共同引用一个地址，对l2进行了同样的计算，形成一个新的列表

for i in range(4):
    for j in range(4):

        l[i][j]=int(uniform(-100,100))
        l1[j][i]=l[i][j]            #进行矩阵的转置运算

print('原矩阵为：')
for i in range(len(l)):
    print(l[i])
print('转置后的矩阵为：')
for i in range(len(l1)):
    print(l1[i])