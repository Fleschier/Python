lst=list(range(2,501))

i=0
while i <len(lst):                          #从列表中取出一个数，从2开始，将后面所有是这个数的倍数的数从列表中删除，循环全部结束后剩下的就是素数
    j=i+1                                    #保证j始终比i大一
    while j<len(lst):
        if lst[j]%lst[i]==0:
            del lst[j]
            j-=1                             #因为删除一个元素后，后面的元素会向前补齐，所有需要将索引值减一
        j+=1
    i+=1                                     #取出列表中下一个数，继续上面的循环

count=0
for i in lst:
    print('{:<8d}'.format(i),end=' ')
    count+=1
    if count%5==0:
        print()                             #格式化输出数据