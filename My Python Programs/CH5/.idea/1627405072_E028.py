x=input('请输入字符串：')

n=int(input('请输入需要删除第几个字符：'))

if 0<n<=len(x):                                   #确保输入的n在字符串长度限制之内
    print('{}{}'.format(x[0:n-1],x[n:len(x)]))  #输出删除后的字符

else:
    print('invalid number')