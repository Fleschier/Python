list=[('张飞',('高数',78),('线代',75))]
list.append(('李大刀',('高数',92),('线代',67)))
list.append(('李墨白',('高数',84),('线代',88)))
list.append(('王老虎',('高数',50),('线代',50)))
list.append(('雷小米',('高数',99),('线代',98)))    #将数据录入列表


temp1=[]                                             #进行一些变量的初始化
temp2=([0]*5)
sum=0
for i in range(5):                                  #将每个人高数和线代的成绩录入列表
    sum=list[i][1][1]+list[i][2][1]
    temp1.append(sum)

temp1=sorted(temp1,reverse=True)                     #将成绩从大到小排序

for i in range(5):
    sum=list[i][1][1]+list[i][2][1]
    temp2[temp1.index(sum)]=list[i]                  #利用排序后总成绩的位置索引，将成绩对应的人的信息按顺序录入一个新列表并输出

for i in range(5):
    print(temp2[i])
