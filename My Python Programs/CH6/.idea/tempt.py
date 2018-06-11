l=list(range(2,501))        #设置一个list对象
count=-1                    #设置计数器
for i in range(2,501):

    count = count + 1

    for j in range(2,i):

        if i%j==0 and i!=2:
            del l[count]    #删去list对象里面所有的非质数
            count=count-1
            break

count=0
for k in l:
    print('{0:<10d}'.format(k),end='')
    count=count+1
    if count%5==0:
        print()             #格式化输出list中的数字

print()