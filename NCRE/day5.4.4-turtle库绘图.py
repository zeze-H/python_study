import turtle as t

t.setup(600, 600, 10, 10)
t.pensize(2)

# 画笔速度
t.speed(10)

# 画一个半径60、角度为280的圆（默认逆时针）
t.circle(60, 280)

# 画半径为100的内切多边形
t.circle(100, steps=6)

# 画笔移动到指定坐标
t.goto(60, 100)

# 修改画笔的横坐标到 x，纵坐标不变
t.setx(0)

# 修改画笔的纵坐标到 y，横坐标不变
t.sety(0)

# 设置当前朝向角度：setheading() / seth()
t.seth(90)

# 画笔位置回到原点，并朝向东
t.home()

# 绘制指定直径和颜色的点
t.dot(20, "red")
