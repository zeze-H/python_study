# '''函数'''
# #创建函数
# def myfunc():
#     pass
#
# def myfunc2():
#     for i in range(6):
#         print("hello zeze")
# myfunc2()

# #函数的参数
# #参数实现函数个性化定制
# def myfunc3(name):
#     for i in range(3):
#         print(f"i am {name}")
# myfunc3("zeze")
# #形式参数：name,times和实际参数:zeze,3
# def myfunc4(name,times):
#     for i in range(times):
#         print(f"i am {name}")
# myfunc4("zeze",3)

# #函数的返回值:return
# def div(x,y):
#     z=x/y
#     return z
# print(div(4,2))
# #除数不能为0，做以下修改：
'''只要执行了return语句，函数就会直接返回，不会继续执行'''
from idlelib.debugobj import myrepr

# def div2(x,y):
#     if y==0:
#         return "除数不可以为0"
#     else:
#         return x/y
# print(div2(4,0))
# '''如果没写return,函数也会返回一个none'''
# def myfunc():
#     pass
# print(myfunc())

'''细讲函数参数'''

# # #位置参数:在函数内定义参数位置
# def myfunc(s,vt,o):
#     return"".join((o,vt,s))
# print(myfunc("我","爱","你"))

# #关键字参数:对于参数多的函数，不会记错位置
# print(myfunc(o="我",vt="爱",s="你"))

# #同时使用位置参数和关键字参数时，位置参数必须在关键字参数之前
# print(myfunc('我',"爱",o='你'))

# #默认参数：如果没有传入实参，就用默认参数，默认参数也必须放在位置参数之后
# def myfunc(s,vt,o='你'):
#     return"".join((o,vt,s))
# print(myfunc('香蕉','吃'))

# # #无论是系统函数还是自定义函数，‘/’斜杠左边不支持自定义函数：
# def abc(a,/,b,c):
#     print(a,b,c)
# abc(1,2,3)
# # # #下面这行会报错
# # abc(a=1,2,3)
# abc(1,b=2,c=3)
# # #'*'星号的右侧只能是关键字参数，才不会报错：
# '''星号相当于匿名的收集参数,下面有收集参数详细资料'''
# def abc(a,*,b,c):
#     print(a,b,c)
# abc(a=1,b=2,c=3)
# # # #下面这行会报错
# abc(1,2,3)

# # *args收集参数:收集任意数量的位置参数，并打包成一个元组
'''收集参数可以保证输入多个实参而不报错,如果形参有三个，实参有四个，就会报错'''
# def myfunc(*args):
#     # args 是一个元组，len(args) 表示传入的参数个数
#     print("有{}个参数".format(len(args)))
#     print("第2个参数是{}".format(args[1]))
# myfunc(1,2,3,4,5)
# def myfunc(*args):
#     # 直接打印 args，可以看到所有位置参数被打包成的元组
#     print(args)
# myfunc(1,2,3,4,5)

# def myfunc():
#     return(1,2,3)
# myfunc()
# x,y,z = myfunc()
# print(x,y,z)
'''
"*"星号作用:进函数打包，出容器解包
左边收集，右边展开
'''
# def myfunc(*args):
#     print(type(args))
# myfunc(1,2,3,4,5)
'''如果使用收集参数后还需要使用其他参数,就必须指定关键字参数'''
# # *args 抢走了所有剩下的位置参数，所以后面的参数不能再用位置方式传入，必须用关键字明确指定。
# def myfunc(*args,a,b):
#     print(args,a,b)
# myfunc(1,2,a=3,b=4)

''''**'双星号可以打包成字典,传入实参必须传入关键字参数,因为字典是键值对出现'''
# def myfunc(**kwargs):
#     print(kwargs)
# myfunc(a=1,b=2,c=3)

#混合写法:
# def myfunc(a,*b,**c):
#     print(a,b,c)
# myfunc(1,2,3,4,c=5,d=6,e=7)
# #.format方法就是混合写法:
# help(str.format)

# # #解包参数:
# args=(1,2,3,4)
# def myfunc(a,b,c,d):
#     print(a,b,c,d)
# # #带星号会被解包,如果直接输入args会因为函数需要四个参数,但是只给了一个参数而报错
# # myfunc(args)
# myfunc(*args)
# #关键字参数解包:**
# kwards={'a':1,'b':2,'c':3,'d':4}
# myfunc(**kwards)

# #作用域
# #局部作用域:在函数内部定义变量
# def myfunc():
#     x=520
#     print(x)
# myfunc()
# #全局作用域:定义全局变量
# y=880
# def myfunc():
#     print(y)
# myfunc()

# #在函数中,局部变量会覆盖全局变量,但是只要出了函数,局部变量就会失效
# x=880
# def myfunc():
#     x=520
#     print(x)
# myfunc()
# print(x)

# #global语句:将函数内的局部变量修改成全局变量
# x=880
# def myfunc():
#     global x
#     x=520
#     print(x)
# myfunc()
# print(x)


# #嵌套函数
# def funA():
#     x=520
#     #如果想调用funB,只能通过funA
#     def funB():
#         x=880
#         print("in funB,x=",x)
#
#     print("in funA,x=",x)
#     funB()
# funA()
#
# # nonlocal:内部函数修改外部函数的变量
# def funA():
#     x=520
#     def funB():
#         nonlocal x
#         x=880
#         print("in funB,x=",x)
#     funB()
#     print("in funA,x=",x)
# funA()

#legb规则：
'''
L:local:局部作用域
E:enclosed:嵌套函数外层函数作用域:nonlocal
G:global:全局作用域:global
B:build-in:内置作用域
python会根据legb的顺序依次查找变量名
'''
# #内置作用域:Python 自带的名字仓库
# str="str被毁掉了"
# #str函数可以将一个数字转换为字符串,但是str已经作为一个变量名存在
# # print(str(520))
# print(str)
# print(type(str))

#闭包
'''闭包的引用'''
# def myfunc():
#     x=520
#     print(x)
# myfunc()
#如果再次print(x)则会报错，因为myfunc已经调用结束

# def funA():
#     x=880
#在这里本质上funB是不能再次printx的，但是：
'''因为内层函数用到了外层变量，所以 Python 不会销毁这些变量，而是把它们和内层函数一起保存起来。'''
#     def funB():
#         print(x)
#     funB()
# funA()

# #不通过funA函数来调用funB
# def funA():
#     x=880
#     def funB():
#         print(x)
#     return funB
# '''funB函数的引用'''
# print(funA())
# #调用funB就可以如下写法：
# funA()()
# funny=funA()
# #这样就可以使用funny来间接调用funb
# funny()
'''本质上funA已经不具备funB了 但是却能够通过间接的方式用funny来呈现'''

'''对于嵌套函数来说，外层函数的定义域:x是会通过某种形式给保存下来的尽管这个函数已经调用完了。
但是并不会像局部定义域调用完就消失了'''
'''当内层函数引用了外层函数的变量时，外层函数的局部变量不会随着函数执行完毕而销毁，
而是会被内层函数「捕获」并「保存」下来，形成一个 “封闭的环境”（这就是「闭包」名字的由来）。'''


# #什么是闭包：工厂函数
# #做一个次方和立方的计算器
# def power(exp):
#     def exp_of(base):
#         return base ** exp
#     return exp_of
# square=power(2)
# cube=power(3)
# print(square(3))
# print(cube(2))
# #做一个有记忆存储功能的加法器
# def outer():
#     x=0
#     y=0
#     def inner(x1,y1):
#         nonlocal x,y
#         x+=x1
#         y+=y1
#         print(f"现在，x={x},y={y}")
#     return inner
# move=outer()
# move(1,2)
# move(-2,2)

# # 装饰器
# def myfunc():
#     print("正在调用mufunc")
# def report(func):
#     print("主人，我要开始调用函数了...")
#     func()
#     print("主人，我调用完函数啦，快夸夸我。")
# report(myfunc)

import time
def time_master(func):
    print("开始运行程序")
    start=time.time()
    func()
    stop=time.time()
    print("结束程序运行...")
    print(f"一共耗费了{(stop-start):.2f}秒")
def myfunc():
    time.sleep(2)
    print("Hello zeze")
time_master(myfunc)

