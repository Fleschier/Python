dic={}

print("如需结束请输入'END'")
while True:                                         #录入雇员姓名

    a=input('请输入姓名：')

    if a=='END':
        break
    b = input('请输入编号:')
    if b == 'END':
        break
    dic[a] = b

names=dic.items()                                     #将雇员姓名和编号从字典中取出按元组放入列表排序
names=sorted(names,key = lambda s : s[0])            #以列表每个元素的第一个元素，即姓名进行排序
print('按姓名排序：')
for i in names:
    print(i)

print('按编号排序：')
names=sorted(names,key= lambda s : s[1])             #以列表的第二个元素，即编号进行排序
for i in names:
    print(i)