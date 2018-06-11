x=input('请输入字母：')
c=ord(x)            #返回字符的ACSII码值
if 65<=c<=90:
    c=c+32          #如果是大写字母，则将ASCII码值加上32得到对应的小写字母的ASCII码值
    print(chr(c))   #由ASCII码值返回到字符
elif 97<=c<=122:
    c=c-32          #如果是小写字母，则将ACSII码值加上32得到对应的大写字母的ACSII码值
    print(chr(c))   #由ASCII码值返回字符
else:
    print(x)