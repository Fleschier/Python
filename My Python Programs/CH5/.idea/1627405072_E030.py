x=input('请输入一个字符串：')

count=0
s=''
for a in x:                                            #设置a在x中的循环
    if a in s:
        continue

    n=x.count(a,0,len(x))
    s=s+a

    print('\'{}\':{}'.format(a,n),end=',\t')         #格式化输出各个字符的个数

    count = count + 1
    if count % 5 == 0:
        print()