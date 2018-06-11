x,y,z=eval(input('输入x,y,z:'))
max=x if x>=y else y        #先判断x和y的大小，并将较大值赋给max
max=z if z>=max else max    #如果比较z与max的大小，并将较大值赋给max
print(max)

