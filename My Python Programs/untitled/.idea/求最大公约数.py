def main():
    a,b=eval(input('请输入两个数：'))
    if a <= b:
        a, b = b, a
        LargestDivision(a, b)
    else:
        LargestDivision(a, b)


def LargestDivision(a,b):
        while True:
            a=a%b
            if a==0:
                print('最大公因数为：',b)
                break
            b=b%a
            if b==0:
                print('最大公因数为：', a)
                break
main()