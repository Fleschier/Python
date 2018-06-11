n=eval(input('输入整数n:'))

for k in range(1,n+1):
    print('   {0:>6d}'.format(k),end='\t')                  #首先输出第一行数
print()                                                        #输出结束后转行

for i in range(1,n+1):                                        #进入输出乘法表的循环

        print( '{0:<6d}'.format(i),end='\t')                 #输出第一列数

        for j in range(1,i+1):
            print( '{0:<6d}'.format(j * i),end='  \t')       #输出相乘的结果，并且控制格式和输出的个数
        print()                                                #一串数据输出结束后转行
