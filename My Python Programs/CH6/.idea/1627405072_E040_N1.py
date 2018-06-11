n=int(input('请输入奇数n：'))
matrix=[[0]*n for i in range(n)]    #创建一个全零矩阵以便下面存放数据
numbers=range(1,n**2+1)

a=0
b=(n-1)//2
for i in numbers:                   #从1到n的平方，依次按魔方阵的填写规则填入矩阵
    if matrix[a][b]!=0:             #按照填写规则，如遇到已填过的空，便退一格到下方
        a+=2
        b-=1
        matrix[a][b]=i
        a-=1
        b+=1
    else:
        if a<=n-1 and b<=n-1:       #以矩阵副对角线依次填数字，遇到越界则换边或跳列
            matrix[a][b]=i
            a-=1
            b+=1
            if a<0 and b>n-1:
                a+=2
                b-=1
            elif a<0:
                a=n-1
            elif b>n-1:
                b=0
for i in matrix:                    #输出矩阵
    print(i)