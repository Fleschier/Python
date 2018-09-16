# python中print是默认换行的
def main():
    expression = input("Please enter an expression: ")
    inputArr = list(expression)  # 使用list(str)就能将一个string转化为char的list,并且是每个字符一个元素，多个空格也会拆分开
    print(inputArr)
    parser = Parser(inputArr)
    parser.conversion()


class Parser:
    index = -1
    length = 0
    inputArr = []
    flag = 1

    # self代表当前类的实例对象，而不是类，self.class指向类
    # 构造函数
    def __init__(self, inputarr):
        self.inputArr = inputarr
        if(len(inputarr) != 0):
            self.length = len(inputarr)

    # 读取下一个输入字符
    def readNext(self):
        if(self.index < self.length - 1):
            self.index += 1
            # 去除输入中的可能出现的所有空格
            while(self.inputArr[self.index] == " "):
                self.index += 1
            return 1
        else:
            return -1

    # 读取下一个数字(考虑到可能不止一位)
    def readNextDigit(self):
        self.flag = self.readNext()
        tmp = ""
        while (str.isdigit(self.inputArr[self.index])):
            tmp += self.inputArr[self.index]
            self.flag = self.readNext()
            if (self.flag == -1): break
        return tmp

    # 转换函数，将中缀表达式转化为后缀表达式
    def conversion(self):
        while(self.flag == 1):
            if(str.isdigit(self.inputArr[self.index])):
                tmp1 = self.readNextDigit()
                print(tmp1, end=" ")
            elif(self.inputArr[self.index] == '+'):
                tmp2 = self.readNextDigit()
                print(tmp2, end=" ")
                print("+", end=" ")
            elif(self.inputArr[self.index] == '-'):
                tmp3 = self.readNextDigit()
                print(tmp3, end=" ")
                print("-", end=" ")
            else:
                print("This is an invalid syntax for this converter!")


main()
