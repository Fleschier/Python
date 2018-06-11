import re
s="I'm   a   student,i   want, to   study.The student,djf!sd."
punctuation=".,!;:"    #存放标点符号
pattern=re.compile("\s\s+")
s=pattern.sub(" ",s)      #去除原始的字符串s中多余的空格
count=0   #用于在向s中插入空格时调整下标使用
for itr in re.finditer("["+punctuation+"]",s):     #找到s中所有标点符号的迭代器
    # 可以使用print(itr.group(),i.span())查看标点符号的情况 
    index=itr.span()[0]+count    #itr.span()[0]为标点符号在原始的s中的下标，count表示插入空格的个数
    if index<len(s)-1:     #此时说明这个标点符号不是字符的结尾，就是过滤掉字符串结尾的标点符号 
        temp=s[index+1]      #取出标点符号后面的字符
        #当标点符号后面的字符是字母的时候，才会插入空格
        if (ord(temp)>=ord("A") and ord(temp)<=ord("Z")) or (ord(temp)>=ord("a") and ord(temp)<=ord("z")):
            s=s[0:index+1]+" "+s[index+1:]     #使用切片的方法产生新的字符串
            count+=1     #插入的空格数加1
print(s)
