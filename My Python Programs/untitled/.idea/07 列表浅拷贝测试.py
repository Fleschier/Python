#a1、a2为出错的二维列表
#a3、a4为正常的二维列表
#a11、a12为单行的列表
#三类分别测试了初始值为None或0是否有影响
a1=[[None]*4]*4
a2=[[0]*4]*4

a3=[[None]*4 for i in range(4)]
a4=[[0]*4 for j in range(4)]

a11=[None]*4
a12=[0]*4

for i in range(4):
    for j in range(4):
        #先分别赋值
        a1[i][j]=(i+1)*(j+1)
        a2[i][j]=(i+1)*(j+1)
        a3[i][j]=(i+1)*(j+1)
        a4[i][j]=(i+1)*(j+1)
        print("第{}.{}轮：".format((i+1),(j+1)))
        print("a1:")
        for k in range(4):
            print("id={} {}".format(id(a1[k]),a1[k]))
        print("a2:")
        for k in range(4):
            print("id={} {}".format(id(a2[k]),a2[k]))
        print("a3:")
        for k in range(4):
            print("id={} {}".format(id(a3[k]),a3[k]))
        print("a4:")
        for k in range(4):
            print("id={} {}".format(id(a4[k]),a4[k]))
    #单行列表a11、a12的赋值
    a11[i]=i+1
    a12[i]=i+1
    print("a11:\n{}".format(a11))
    for j in range(4):
        print("id{}={}".format(j+1,id(a11[j])))
    print("a12:\n{}".format(a12))
    for j in range(4):
        print("id{}={}".format(j+1,id(a12[j])))
    print()

#结果看起来应该0和None没有影响
#单行列表里的元素并不是浅拷贝
#a1、a2赋值出错原因确实是浅拷贝的问题