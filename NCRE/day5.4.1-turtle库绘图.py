# 窗体函数的三种调用方法
'''
import turtle  # 从左到右依次是窗口长、宽、距离左侧距离、顶部距离（单位：像素）
turtle.setup(600, 600, 10, 20)
'''

import turtle as t
t.setup(600, 600, 10, 20)

'''
from turtle import *
setup(600, 600, 10, 20)
'''

# 前进 forward() / fd()
# 后退 backward() / bk()

# t.forward(100)
t.fd(200)
t.backward(100)
t.bk(100)

# 向右转角度：right()
# 向左转角度：left()
'''
t.left(90)
t.right(180)
'''

# 画一个正方形
for i in range(4):
    t.fd(100)
    t.left(90)
