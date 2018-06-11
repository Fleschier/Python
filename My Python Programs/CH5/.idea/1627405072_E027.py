s=input('请输入一个字符串：')

if len(s)<=2:                                 #讨论字符串长度小于2的情况
    print('')

else:
    print('{}{}'.format(s[0:2],s[-2:]))     #输出新字符串