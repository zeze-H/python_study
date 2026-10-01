#最简单的闭包
def myfunc():
    a=1
    def funa():
       print(a)
    return funa
hello = myfunc()
hello()

#闭包创建工厂函数:
def power(x):
    def inner(y):
        c = y**x
        print(c)
    return inner
#算平方
end = power(2)
end(2)
#算立方
end2 = power(3)
end2(2)

#闭包的记忆功能:
#内存函数记住外层函数作用域并修改
def outer():
    a=0
    b=0
    def inner(x1,y1):
        nonlocal a,b
        a+=x1
        b+=y1
        print(f"现在a等于{a},b等于{b}")
    return inner
result = outer()
for i in range (10):
    result(1,1)

