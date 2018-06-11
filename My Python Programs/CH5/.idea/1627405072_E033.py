x=input('请输入单行XML/HTML，按回车继续输下一行（输入单独的‘end’结束输入）：')

s=''
while x!='end':                             #使用循环语句输入多行HTML代码
    s=s+x+'\n'
    x = input('请输入单行XML/HTML，按回车继续输下一行（输入单独的‘end’结束输入）：')

import re
p1=re.compile('<(\w*)>')                   #匹配开头的尖括号
p2=re.compile('</(\w*)>')                   #匹配末尾的尖括号

s=p1.sub(r'\1:',s)
s=p2.sub('',s)
print(s)