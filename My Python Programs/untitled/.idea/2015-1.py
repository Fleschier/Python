x=int(input('Please inpit an int number:'))
if x%3==0 and x%4==0:
    print('{0} could be divided by 3 and 4'.format(x))
else:
    print('{0} could not be divided by 3 or 4'.format(x))

b=str(x)
a=len(b)
c=b [-1:-len(b)-1:-1]
c=int(c)
print('整数{0}是一个{1}位的整数，其逆序数为{2}'.format(x,a,c))

count=0         #设置计数器
print('整数所有非质数因子为：')
for i in range (2,x):
    m=x%i
    if m==0:            #挑选出x的因子
        for j in range(2,i):
            if i%j==0:      #挑选出因子中的非质数因子
                print('{0:<5d}'.format(i),end='')
                count=count+1
                if count%5==0:
                    print()
                break   #及时终止，避免循环中满足不断条件而重复输出同一个数

print()


#选做题部分


count1=0

max=0
min=100
sum=0
for i1 in range (1,1000):
    a1=0
    b1=0

    for j1 in range(2,i1):
        if i1%j1==0:

            if j1%2==0: a1=a1+1
            else: b1=b1+1

    if a1>=5 and b1>=4:
                print('{0:>6d}'.format(i1),end='')
                count1=count1+1
                if count1%10==0:
                    print()

                if min>=i1:
                    min=i1
                elif max<=i1:
                    max=i1

                sum=sum+i1

print()

average=(sum-max-min)/(count1-2)
print('所有整数平均值为{0:0.3f}'.format(average))
