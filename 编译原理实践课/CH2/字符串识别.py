import re

def main():
    # data = input("please enter a string: ")
    # verifyStr(data)
    # isLower(data)
    # matchName(data)
    # matchEmAds(data)
    # matchValidUrl()
    infile = open("redata.txt")
    # readAndProcess(infile)
    ExtractEmail(infile)
    infile.close()


# 1
def verifyStr(data):
    p = re.compile("(s[0-9]).*([bh][aiu]t).*", re.M)
    resLst = p.findall(data)
    for i in resLst:
        print(i[0], ":", i[1])

# 2
def isLower(data):
    pre = re.compile("(s[0-9]) = \'(\w+)\'", re.M)
    p = re.compile("^[a-z]+$")
    resLst = pre.findall(data)
    for i in resLst:
        tmp = p.search(i[1])
        if(tmp):
            if(tmp.group() == i[1]):
                print(i[0], ":", i[1], "全为小写")
        else:
            print(i[0], ":", i[1], "不全为小写")


# 3
def matchName(data):
    p = re.compile("(\w+), (.+)")
    res = p.search(data)
    if(res):
        print("Your first name is: ", res.group(1), "\n", "your second name is: ", res.group(2))
    else:
        print("invalid input!")


# 4
def matchEmAds(data):
    p = re.compile("\w+@(\w+\.?)+")
    res = p.search(data)
    if(res):
        print("'{}' is an E-mail address.".format(res.group()))
    else:
        print("invalid E-mail address")


# 5
def matchValidUrl():
    str="http://www.suda.edu.cn ， https://vpn.suda.edu.cn ， http://weibo.cn ，http://nlp.suda.edu.cn/~wangzq/bianyi/index.html"
    p = re.compile("(https?://(/?~?\w+\.?)+)")
    resLst = p.findall(str)
    for i in resLst:
        print(i[0])


# 6
def readAndProcess(infile):
# 统计一周每天出现的次数
    data = infile.read()
    # Statictic = dict()
    dayLst = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i in dayLst:
        p = re.compile(i)
        lens = len(p.findall(data))
        # Statictic[i] = lens
        print("{} : {}".format(i, lens))

# 提取每一行的Email
def ExtractEmail(infile):
    dataLst = infile.readlines()
    emailP = re.compile("((\w+)@((\w+\.?)+))")
    for line in dataLst:
        tmp = emailP.findall(line)
        for i in tmp:
            print(i[0])
            # 提取登录名和域名
            print("登录名： {}".format(i[1]))
            print("域名： {}".format(i[2]))


main()
