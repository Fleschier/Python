# # from urllib.request import urlopen
# # import gzip
# # html=urlopen("http://www.bilibili.com/video/av10388972/?from=search&seid=11966602115491490193")
# # print(html.read().decode(encoding='utf-8')) #这里无法解码因为获得的网页是压缩过的。。。。
# # url=r"http://www.bilibili.com/video/av10388972/?from=search&seid=11966602115491490193"
# # url=urlopen(url).geturl()                                   #防止重定向，获取其真实的url
# # html=(urlopen(url))
# # print(html.info())                                          #得到Content-Encoding:gzip得知其使用gzip的压缩网页的方式（坑了两天才发现-_-）
# # def getUrlContent(url):                                     # 得到页面内容
# #     data = urlopen(url).read()                              #得到的文件只能读取一次
# #     # 解码过程
# #     try:
# #         html = gzip.decompress(data).decode("utf-8")         #先解压再解码
# #     except:                                                  #如果解压不成功则直接解码
# #         html = data.decode("utf-8")
# #     return html
# # data=getUrlContent(url)
# # infile=open("Rawdata.txt","w",encoding="utf-8")
# # infile.write(data)
# # print(data)
# # 然而要获取弹幕，需要运用到动态网页抓取，前面的只是徒劳-_-..，以上是失败的历史



# #下面才是重点代码
# #http://comment.bilibili.com/rolldate,17158352.这个是储存所有历史弹幕的地址
# #http://comment.bilibili.com/dmroll,1495209600,17158352（用第一个url里面储存的数字代替这里面的第一个数字即可得到不用的储存弹幕的地址）
# #以上是动用了bilibili会员才获得的历史弹幕-_-..
# #获取弹幕的来源地址是通过在Chrome浏览器中查看其来源（快捷键F12调出开发者选项）

#-----------------------------------------------------------------------------------------------------------------------
####下面是分块一 ---------------------------------------------------------------------------------------------------------
import requests         #需要在cmd中输入：pip3 install requests来安装。用了requests库才知道urllib的方法多low。。
import re
url1=r"http://comment.bilibili.com/rolldate,17158352"
file1=requests.post(url1)#一般post获取到的数据量的限制比get要宽松，所以能获得更多的数据

pnum=re.compile('\d{10,}')
numlst=pnum.findall(file1.text) #将第一个地址中所有存储地址的数字录下来记录在列表里
# print(numlst)

'''资料：
几个主要非英文语系字符范围
2E80～33FFh：中日韩符号区。收容康熙字典部首、中日韩辅助部首、注音符号、日本假名、韩文音符，中日韩的符号、标点、带圈或带括符文数字、月份，以及日本的假名组合、单位、年号、月份、日期、时间等。
3400～4DFFh：中日韩认同表意文字扩充A区，总计收容6,582个中日韩汉字。
4E00～9FFFh：中日韩认同表意文字区，总计收容20,902个中日韩汉字。
A000～A4FFh：彝族文字区，收容中国南方彝族文字和字根。
AC00～D7FFh：韩文拼音组合字区，收容以韩文音符拼成的文字。
F900～FAFFh：中日韩兼容表意文字区，总计收容302个中日韩汉字。
FB00～FFFDh：文字表现形式区，收容组合拉丁文字、希伯来文、阿拉伯文、中日韩直式标点、小符号、半角符号、全角'''

infile1 = open("所有弹幕.txt", 'w',encoding='utf-8')      #指明文件的编码方式为utf-8，与获得的网页数据一致，否则系统会默认为gbk编码
for i in range(len(numlst)):
    url2="http://comment.bilibili.com/dmroll,"+numlst[i]+",17158352"
    file2=requests.post(url2)

    #第一遍用正则表达式提取出所有中文字符
    pattn=re.compile('[\u2E80-\uFFFDh]+')
    lst=pattn.findall(file2.text)
    #第二遍用正则表达式去掉所有的标点符号
    p=re.compile('\w+')
    st='\n'.join(lst)
    datalst=p.findall(st)
    ##不知道为什么总是有五个'h'。。。。。滑稽

    for obj in datalst:
        infile1.write(obj+"\n")
    #print(datalst)
    datalst.clear()

infile1.close()
#以上是先将所有弹幕都提取出来写入文件，否则内存根本放不下。。。--------------------------------------------------------------------


#下面是分块二 ------------------------------------------------------------------------------------------------------------
try:
    infile2=open("stopwords.txt","r")                       #这个用默认读取方式即可
    infile3=open("所有弹幕.txt","r",encoding='utf-8')       #这个由于写入时用的是utf-8，所以读取时也要制定为utf-8
except:
    print('File is not found!')
    exit()

stplst=[]       #存放所有的停用词
swd=infile2.readline()
while(swd):
    swd=swd.strip(' \n')
    stplst.append(swd)
    swd=infile2.readline()
stplst.sort(reverse=True,key=len)       #将停用词从长到短排序，再进行分词

infile4=open("第一次处理后的弹幕.txt","w",encoding='utf-8')
words=infile3.readline()
while(words):
    words=words[:-1:]               #此处去掉换行符
    for s in stplst:
        if(s!=''):                   #最后居然有几个空行。。。。果然有坑
            tmp=words.split(s)
            if len(tmp)>=2:
                break
        elif(s==''):
            continue
    for s in tmp:
        infile4.write(s+'\n')
    words = infile3.readline()

infile2.close()
infile3.close()
infile4.close()
# #以上是对弹幕的初次处理，还残留大量的空格空字符串什么的-------------------------------------------------------------------------


#分块三------------------------------------------------------------------------------------------------------------------
infile=open("第一次处理后的弹幕.txt","r",encoding='utf-8')
infile1=open("第二次处理后的弹幕.txt","w",encoding='utf-8')
tp=infile.readline()
while(tp):
    if tp[0]!='\n':             #去掉所有空行
        infile1.write(tp)
    tp=infile.readline()
infile.close()
infile1.close()
# #第二次处理弹幕，下面就是进行统计词频---------------------------------------------------------------------------------------

#分块四 -----------------------------------------------------------------------------------------------------------------
data={}
file=open("第二次处理后的弹幕.txt","r",encoding='utf-8')
tps=file.readline()
while tps:
    tps = tps[:-1:]
    if tps not in data:
        data[tps]=0
    else: data[tps]+=1
    tps=file.readline()

sdata=sorted(data.items(),key=lambda x:x[1],reverse=True)        #这里的d.items()实际上是将d转换为可迭代对象，迭代对象的元素为(键，值)，所以对第二个元素排序
print(sdata)                                                     #此处sdata为列表

#写入json文件
import json
file=open("结果.json","w",encoding='utf-8')
json_str=json.dumps(data)       #将字典转化为字典样子的字符串
file.write(json_str)
file.close()

#由于程序处理的文件太大，运行需要将近一分钟的时间，可以按照我分好的部分分块运行。。。滑稽-----------------------------------------------
#由于最近实在事情多，所以JavaScript的部分就没时间写了。。。