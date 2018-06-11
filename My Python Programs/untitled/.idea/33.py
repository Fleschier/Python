#coding:utf-8
import re
s="""<composer>WolfgangAmadeus Mozart</composer>
     <author>SamuelBeckett</author>
     <city>London</city>"""
pattern1=re.compile("<\w+>")   #匹配<>中任意的字符
pattern2=re.compile(">.+</")   #匹配><中任意的字符
listNames=pattern1.findall(s)  #获取所有满足正则表达式pattern1的字符串的列表
listContents=pattern2.findall(s)  #获取所有满足正则表达式pattern2的字符串的列表
#由于xml是规范的，所以是一一对应（对于错误输入，暂时不考虑）
for i in range(len(listNames)):
    #输出的时候利用切片丢弃多余的符号，如：<>/
    print(listNames[i][1:len(listNames[i])-1],":",
          listContents[i][1:len(listContents[i])-2])

