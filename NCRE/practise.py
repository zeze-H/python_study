from turtle import *

setup(600,600,200,200)
pensize(2)
pencolor("red")
color("red","blue")
forward(300)
backward(300)
left(90)
right(90)
clear()
hideturtle()
begin_fill()
for i in range(4):
    fd(200)
    right(90)
end_fill()
showturtle()
reset()
write("love",font=("仿宋",24))

