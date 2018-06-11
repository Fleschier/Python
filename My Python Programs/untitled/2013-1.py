count=0
max=0
min=100
k=0
sum=0

for i in range(2,1000):
    for j in range(2,i):
        if i%j==0 and i!=2:
            break
    else:
        print('{0:<5d}'.format(i),end='')
        count=count+1

        b=str(i)
        c=b[::-1]
        d=int(c)

        if min>=d:min=d
        elif max<=d:max=d
        k=k+1
        sum=sum+i

    if count==10:
            print()
            count=0

print()

average=(sum-max-min)/(k-2)
print('转换后去最大最小后的平均数为：',average)