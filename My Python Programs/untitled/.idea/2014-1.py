count=0
max=0
for i in range(1,1001):
    m=0
    for j in range(1,i):
        if i%j==0:
            m=m+j
    if m==i:
        print('{0:<5d}'.format(i),end='')
        count=count+1
        if max<=m:
            max=m
    elif count==10:
        print()
        count=0

print()

sum=0
count1=0
for i in range(1,max+1):
    if max%i==0:
        print('{0:>5d}'.format(i),end='')
        count1=count1+1
        if count1%8==0:
            print()

        elif '1' not in str(i):               #判断1是否在数字中出现，只能通过转为字符串来实现判断
            sum=sum+i


print()

average=sum/count1
print('平均值为：',average)
