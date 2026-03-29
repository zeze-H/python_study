# def great():
#     for i in range(3):
#         print('你好!')
# print(great())
# def introudce(name,age):
#     print(f"我叫{name},今年{age}岁")
# introudce('zeze',18)
# def add(a,b):
#     return a+b
# print(add(5,3))
# def safe_div(x,y):
#     if y == 0:
#         return "除数不能为0"
#     return x/y
# print(safe_div(10,2))
# print(safe_div(8,0))
# def no_return():
#     pass
# print(no_return())


# def make_sentence(a,b,c):
#     return''.join((a,b,c))
# print(make_sentence('小猫','钓','鱼'))
# print(make_sentence(a='钓',b='鱼',c='小猫'))
# def introduce(name,age,city='西安'):
#     return f'我叫{name},今年{age}岁,来自{city}'
# print(introduce('张三','20'))
# print(introduce('张三','25',city='河池'))
# def add_num(a,/,b,*,c):
#     return ''.join(a+b+c)
# print(add_num('zeze','love',c='huanhuan'))
# # print(add_num('zeze','love','huanhuan'))
# # ‘/’左边必须是位置参数，‘*’右边必须是关键字参数，否则会报错
# def is_even(n):
#     if n % 2 == 0:
#         return'偶数'
#     return '奇数'
# print(is_even(3))
# def print_star(times):
#     for i in range(times):
#         print("*")
# print_star(5)

# def sum_all(*args):
#     return sum(args)
# print(sum_all(1,3,5,7))
# def print_info(**kwargs):
#     print(kwargs)
# print_info(name="zeze", age=18, city="西安")
# def mix_demo(a,*b,**c):
#     print(a,b,c)
# mix_demo(10,20,30,x=1,y=2)
# nums=(4,5,6)
# info={'name':'huanhuan','age':'17'}
# def func1(a,b,c):
#     print(a+b+c)
# func1(*nums)
# def func2(name,age):
#     print(f'{name}今年{age}岁')
# func2(**info)
# def greet(name,times=2):
#     for i in range(times):
#         print(f"你好，{name}!")
# greet('张三')
# greet('李四',times=4)
# def is_positive(n):
#     if n>0:
#         return '正数'
#     elif n<0:
#         return '负数'
#     else:
#         return 0
# print(is_positive(-5))
# print(is_positive(0))

# count=0
# def add_count():
#     global count
#     count+=1
#     return count
# for i in range(2):
#     print(add_count())
# def outer():
#     msg='外部函数'
#     def inner():
#         nonlocal msg
#         msg='内部函数修改后'
#         print(msg)
#     print(msg)
#     inner()
#     print(msg)
# outer()
# '''预期输入：局部
#     原因：先找局部，然后是嵌套函数外部，再是全局，最后是内置'''
# list=[1,2,3]
# # list('abc')
# #内置函数list已经被定义成了列表，无法再次使用
# def calc_avg(*args):
#     return sum(args)/len(args)
# print(calc_avg(2,4,6,8))
# def check_num(n,/,*,flag="奇偶"):
#     if flag=="奇偶":
#         if n%2==0:
#             print('偶数')
#         else:
#             print("奇数")
#     else:
#         if n>0:
#             print('正数')
#         elif n<0:
#             print('负数')
#         elif n==0:
#             print('零')
# check_num(7,flag='正负')
# check_num(10)
# def funA():
#     x = 880
#     print(x)
#
# funA()

#内层函数引用外层函数的变量时，外层函数的局部变量不会随函数执行完毕销毁，而是被内层函数‘捕获’并保存，形成封闭环境，这就是闭包
#legb:程序在查找变量，依次从局部，外层，全局，内置来查找
# def creat_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
# counter = creat_counter()
# for i in range(100):
#     print(counter())

# def creat_grade_manager():
#     grades = []
#     student_name=""
#     def manager(action,*args,**kwargs):
#         nonlocal grades,student_name
#         if action=="set_name":
#             student_name=kwargs.get('name','')
#         elif action=="add_grade":
#             grades.extend(args)
#         elif action=="get_avg":
#             if not grades:
#                 return 0
#             return sum(grades)/len(grades)
#         elif action=="get_info":
#             avg=manager("get_avg")
#             return f"学生：{student_name},成绩：{grades}，平均分：{avg}"
#     return manager
# manager=creat_grade_manager()
# manager("set_name", name="张三")
# manager("add_grade", 85, 90, 78)
# print(manager("get_info"))  # 输出包含姓名、成绩、平均分的信息


def creat_greeter(name):
    def greeter():
        print("Hello, " + name)
    return greeter
a=creat_greeter()


