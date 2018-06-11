lst=[1,213,234,23]

def deco1(func):
    print('列表元素之和为：')
    return func

def deco2(argv):
    def deco3(func):
        print('测试argv：',argv)
        return func
    return deco3

@deco2('成功输出！')
@deco1
def Summary(List):
    return sum(List)

#装饰器定义放在要修饰函数之后会出现未命名错误
# def deco(func):
#     print('列表元素之和为：')
#     return func

print(Summary(lst))