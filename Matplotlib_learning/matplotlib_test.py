import matplotlib.pyplot as plt
import numpy as np

#在调用plt.show()方法后,不能直接savefig否则会得到空白的图片,
# 因为 plt.show() 后实际上已经创建了一个新的空白的图片（坐标轴），
# 这时候你再 plt.savefig() 就会保存这个新生成的空白图片。

#解决方法1:在show()之前保存
#解决方法2:先获取当前图像,
# fig1 = plt.gcf() gcf是获取当前figure的方法
# plt.show()
# fig1.savefig("...")

def main():
    #showPieChart()
    #showHistogram()
    #showCoordinateMap() #still have parameter error
    fig1 = showScatterPlot()
    fig1.savefig("examples.jpg")


#饼状图
def showPieChart():
    labels = ["test1", "test2", "test3", "test4"] #自定义标签
    size = [10, 30, 20, 53]     #每个标签的大小,最后比例由此得出
    explode = (0, 0.2, 0.1, 0.1)    #每个部分离开中心多远
    plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    # autopct，圆里面的文本格式，%1.1f%%表示小数有1位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    plt.axis('equal') #设置x,y轴刻度一致使饼图是圆的
    plt.show()

#直方图
def showHistogram():
    np.random.seed(0) #每次生成的随机数都相同
    avg, sigma = 100, 40
    arr = np.random.normal(avg, sigma, size=1000)
    # 给出均值为mean，标准差为stdev的高斯随机数（场），当size赋值时，例如：size=100，表示返回100个高斯随机数。

    #testArr = [100,24,23,457,24,745,24,76,7564,345,35,234]
    plt.hist(arr, 10, histtype='stepfilled', facecolor='b', alpha=0.75)
    #第一个参数是一个数组, 10是直方图的个数(就是柱体的个数,越多区间划分越细)
    plt.title = ("Histogram_Test")     #设置标题
    plt.show()

#坐标图
def showCoordinateMap():
    N = 20
    theta = np.linspace(0.0, 2*np.pi, N, endpoint=False)
    radii = 10*np.random.rand(N)
    width = np.pi/4*np.random.rand(N)

    ax = plt.subplot(111, projection='ploar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0)

    for r,bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.viridis(r/10.))
        bar.set_alpha(0.5)
    plt.show()

#散点图
def showScatterPlot():
    # fig, ax = plt.subplots()
    # ax.plot(10*np.random.rand(1000), 10*np.random.rand(1000), 'o')
    #ax.set_title("Scatter test")
    x = 10*np.random.rand(1000)       #rand函数产生0~1之间的随机小数
    y = 10*np.random.rand(1000)
    #y = np.cos(x)
    #x,y是点的坐标
    size = np.random.rand(1000)*100     #点的大小
    colour = np.random.rand(1000)       #点的颜色随机产生
    plt.scatter(x, y, size, colour)
    plt.colorbar()

    fig1 = plt.gcf()
    plt.show()
    return fig1

main()
