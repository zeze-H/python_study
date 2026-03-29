import turtle as t

t.setup(600, 600, 10, 20)

t.pensize(2)  # 画笔粗细 pensize() / width()

'''
t.pencolor((1, 0, 0.5))  # 画笔颜色：直接写颜色或者 (r, g, b)
'''

t.color("red", "blue")  # 设置画笔颜色和填充颜色

t.begin_fill()  # 开始填充
for i in range(4):
    t.fd(100)
    t.left(90)
t.end_fill()  # 结束填充

'''
t.clear()  # 清空画板
'''

print(t.filling())  # 填充状态

t.reset()  # 清空画板并重置状态
t.hideturtle()  # 隐藏画笔
t.showturtle()  # 显示画笔

t.write("在画图", font=("仿宋", 12, "normal"))  # 输出字符串并指定字体
