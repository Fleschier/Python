from turtle import *
from time import sleep

def_speed = 10


def go_to(x, y):
    up()
    goto(x, y)
    down()


def big_Circle(size):  # 函数用于绘制心的大圆
    speed(def_speed)
    for i in range(150):
        forward(size)
        right(0.3)


def small_Circle(size):  # 函数用于绘制心的小圆
    speed(def_speed)
    for i in range(210):
        forward(size)
        right(0.786)


def line(size):
    speed(def_speed)
    forward(51 * size)


def heart(x, y, size):
    go_to(x, y)
    left(150)
    begin_fill()
    line(size)
    big_Circle(size)
    small_Circle(size)
    left(120)
    small_Circle(size)
    big_Circle(size)
    line(size)
    end_fill()


def arrow():
    pensize(10)
    setheading(0)
    go_to(-400, 0)
    left(15)
    forward(150)
    go_to(339, 178)
    forward(150)


def arrowHead():
    pensize(1)
    speed(def_speed)
    color('red', 'red')
    begin_fill()
    left(120)
    forward(20)
    right(150)
    forward(35)
    right(120)
    forward(35)
    right(150)
    forward(20)
    end_fill()


def main():
    pensize(2)
    #color('red', 'pink')
    color('#FF0000','#FFCCCC')
    #getscreen().tracer(30, 0) #取消注释后，快速显示图案
    heart(200, -50, 1.7)  # 画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
    setheading(0)  # 使画笔的方向朝向x轴正方向,防止第二颗心方向反掉
    heart(-110, -150, 1.3)  # 画出第二颗心
    #arrow()  # 画出穿过两颗心的直线
    #arrowHead()  # 画出箭的箭头
    #go_to(400, -300)
    go_to(-320, -250)
    write("   嘉琪，\n情人节快乐！\n\n  爱你的\n   翾翾", align="center", font=("楷体", 30, "bold"))
    # go_to(200,-300)
    # write("风里雨里，不忘记你", font=("华文行楷", 20, "normal"))
    done()


main()