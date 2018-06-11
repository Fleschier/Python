a=input('请输入小写字符：')
b=input('请输入小写字符：')

a=set(a)
b=set(b)                 #将两个字符放入集合，通过集合的比较确定是否同构
if a==b:
    print('两个字符同构')

else:
    print('两个字符异构')