import re


# python中有两个很好用的函数 decode() 和 encode()
# decode(‘utf-8’) 是从utf-8编码转换成unicode编码，当然括号里也可以写'gbk'
# encode('gbk') 是将unicode编码编译成gbk编码，当然括号里也可以写'utf-8'


def main():
    indata = "bracketed.gbk.txt"
    resDict = readFileAndProcess(indata)
    print(resDict)


def readFileAndProcess(indata):
    infile = open(indata, "rb")
    resDict = dict()
    oneLine = infile.readline().decode("gbk")       # 将gbk解码为unicode

    while oneLine:
        pattern = re.compile(r"(\w+) ([\u4E00-\u9FFF]+)")       # 匹配中文
        tmpLst = pattern.findall(oneLine)
        for i in tmpLst:
            # print(i)
            if((i[1],i[0]) in resDict):
                resDict[(i[1], i[0])] += 1
            else:
                resDict[(i[1], i[0])] = 1

        oneLine = infile.readline().decode("gbk")

    return resDict


main()

