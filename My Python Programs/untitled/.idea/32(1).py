#coding:utf-8
import re
s="I'm   a   student,i   want, to   study.The student,djf!sd."
punctuation=".,!;:"    #存放标点符号
pattern=re.compile("\s\s+")
s=pattern.sub(" ",s)      #去除原始的字符串s中多余的空格
strList=re.split("(["+punctuation+"])",s)  #使用加强分组的正则对英文短句进行分割
newStr=str()   #此变量用于存放最后修改完成的字符串
#如果当最后一个元素是空的时候就删除它，因为英文短句最后是标点符号，分组时会
#多产生一个空字符
if(strList[len(strList)-1]==''):
    del strList[len(strList)-1]
"""
加强分组后分割得到的列表中，会将作为分割符的标点符号也保留下来的，则一个符合规范
的英文短句在分割后，所有的标点符号都会落在列表中下标为奇数的地方
"""
for index in range(len(strList)):
    if index%2==1:
        newStr+=strList[index]
    else:
        if index!=0:
            tempStr=strList[index][0]   #标点符号后的第一个字符
            #判断标点符号后是不是字母，是就加空格
            if ((ord(tempStr)>=ord('a') and ord(tempStr)<=ord('z'))
               or(ord(tempStr)>=ord('A') and ord(tempStr)<=ord("Z"))):
               newStr=newStr+" "+strList[index]  #标点符号前添加空格
            else:
                newStr+=strList[index]
        else:   #此时index为0，也就是英文短句的开头，不需要烤炉
            newStr+=strList[index]
print(newStr)

