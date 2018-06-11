x=input('请输入一段英文：')

import re
y=re.compile('(\s)+')
m=y.split(x)                #以空格为界分割句子
n=''.join(m[::-1])          #重新组合句子

print(n)