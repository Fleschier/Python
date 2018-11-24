import re


def main():
    data = input("Please enter :")
    # verifyFileName(data)
    # matchDate(data)
    matchPhoneNum(data)
    # readAndExtractHtmlLink("list.html")
    #readAndExtractHtmlPa("content.html")


# 测试文件名
def verifyFileName(str):
    jpg = re.compile(".+\.jpg$", re.I) #re.I忽略大小写
    jepg = re.compile(".+\.jepg$", re.I)
    gif = re.compile(".+\.gif$", re.I)
    bmp = re.compile(".+\.bmp$", re.I)
    all = re.compile("(.+\.)(jpg$|jepg$|gif$|bmp$)") #match all

    if(jpg.search(str)):
        print("This is an jpg file!\n")
    elif(jepg.search(str)):
        print("This is an jepg file!\n")
    elif(gif.search(str)):
        print("This is an gif file!\n")
    elif(bmp.search(str)):
        print("This is an bmp file!\n")
    else:
        print("This is an unidentified File type!")

    if (all.search(str)):
        print("This is an image file\n")


# 匹配时间日期
def matchDate(str):
    datePattern = re.compile("\d{1,2}/\d{1,2}/\d{4}")
    res = datePattern.search(str)
    print(res.group())


# 匹配电话号码
def matchPhoneNum(str):
    pattern = re.compile("\(\d{4}\)\d+-\d{4}")
    resLst = pattern.findall(str)
    for s in resLst:
        print(s)
        print()


# 提取超链接
def readAndExtractHtmlLink(infile):
    infile = open(infile, "r")
    htmlContent = infile.read()
    # pattern = re.compile("<a.*href=\"((\w+://)?(/?\w+\.?)+)\".*>.*</a>")
    p = re.compile(r'<a title="" href="(https://www.sohu.com/a/.+?)" target="_blank">(.+?)</a>')
    # 正则表达式有几个括号，则匹配到的结果每个都是有几个元素的list
    resLst = p.findall(htmlContent)
    # print(len(resLst))
    for link in resLst:
        print(link[0], link[1])
        print()


# 读取段落
def readAndExtractHtmlPa(infile):
    infile = open(infile, "r", encoding="utf-8")  # 这里需要指定编码方式为utf-8，默认为gbk解码会出错
    htmlContent = infile.read()
    prePattern = re.compile("<article.*>.*</article>",re.S)
    p1 = re.compile("<h.*>(.+)</h>")
    p2 = re.compile("<p>(.+)</p>")  # 如果正则表达式只有一个括号则默认匹配的结果就是括号内的
    getAtl = prePattern.search(htmlContent).group()
    print(getAtl, "\n")
    resLst1 = p1.findall(htmlContent)
    resLst2 = p2.findall(getAtl)
    print("Titles:")
    for content in resLst1:
        print(content, end=" ")
        print()
    print("article:")
    for content in resLst2:
        print(content, end=" ")
        print()


main()
