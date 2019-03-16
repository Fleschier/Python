import turtle
import time


def go_to(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

# 画爱心的顶部
def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)

# 输入表白的语句，默认I Love youhexo
love = "      嘉琪\nI LOVE YOU"

me = "cyx"

# 窗口大小
turtle.setup(width=900,height=500)
# 颜色
turtle.color('#FF0000', '#FFCCCC')
# 笔粗细
turtle.pensize(3)
# 速度
turtle.speed(1)
# 提笔
#turtle.up()
# 隐藏笔
turtle.hideturtle()

time.sleep(15)

# 去到的坐标,窗口中心为0,0
go_to(0, -180)

turtle.showturtle()

# 画上线
#turtle.down()

turtle.speed(1)

turtle.begin_fill()

turtle.left(140)

turtle.forward(224)

#调用画爱心左边的顶部
LittleHeart()

#调用画爱右边的顶部
turtle.left(120)
LittleHeart()

# 画下线

turtle.forward(224)

turtle.end_fill()

turtle.pensize(5)

# 在心中写字 一次

go_to(0,-40)

turtle.showturtle()

turtle.color('#CD5C5C','pink')

#在心中写字 font可以设置字体自己电脑有的都可以设 align开始写字的位置

turtle.write(love,font=('华文行楷', 35, 'bold'),align="center")

turtle.hideturtle()

time.sleep(0.5)

# 在心中写字 二次

# 写署名

turtle.color('black', 'pink')

time.sleep(1)

go_to(280,-180)

turtle.showturtle

turtle.write(me, font=('华文行楷', 30), align="center", move=True)

#点击窗口关闭

window=turtle.Screen()

window.exitonclick()