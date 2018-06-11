x=input('请输入一段英文：')

import re
p1=re.compile('\s+')
p2=re.compile(r'([!,.?;:\'\"!])(\w+)')

x=p1.sub(' ',x)
x=p2.sub(r'\1 \2',x)

print(x)