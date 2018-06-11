x=int(input('输入一个三位整数:'))
a=x%10+x%100//10+x//100
print('{0:>4d}'.format(a))