n = eval(input('Please input the number of numbers：'))                                #输入一个数
while type(n) != int :                                                                      #若输入数不合法，则循环显示重新输入
    n = eval(input('Error:Please input the correct type of number：'))


sum = 0                                                                                      #设置一个空的变量存储数的和
for i in range(n):
    x = eval(input('please input number:'))
    sum = sum +int(x)
    while type(x) != int:
        x = eval (input('Error:Please input the correct type of number：'))          #若输入数不合法，则循环显示重新输入
    if x == 0: break                                                                        # 若输入0则循环终止



print('sum:',sum)
