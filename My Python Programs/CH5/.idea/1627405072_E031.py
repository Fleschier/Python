x=input('输入一个英文动词：')

import re
p1=re.compile('y$')
p2=re.compile('[o|ch|s|sh|x|z]$')

m=p1.search(x)
n=p2.search(x)

if m:
    x=p1.sub('ies',x)

elif n:
    x=x+'es'

else:
    x=x+'s'

print('其第三人称单数形式为：',x)