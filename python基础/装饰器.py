# # #将函数作为参数传递
# # def myfunc():
# #     print("调用函数..")
# # def report(func):
# #     print("准备")
# #     func()
# #     print("结束")
# # report(myfunc)
# # #时间管理器
# # import time
# # def time_master(func):
# #     print("开始运行程序...")
# #     start=time.time()
# #     func()
# #     print("程序运行结束...")
# #     end = time.time()
# #     print(f"总运行时间{end-start:.2f}秒")
# # def myfunc():
# #     time.sleep(2)
# # time_master(myfunc)


# import time

# def time_master(func):
#     def myfunc():
#         print("开始运行程序")
#         start=time.time()

#         func()

#         print("程序运行结束")
#         end = time.time()
#         print(f"共耗时{end-start:.2f}秒")

#     return myfunc

# def spend():
#     time.sleep(1)


# spend = time_master(spend)

# spend()
# #语法糖写法:
# # @time_master():
# # def spend():
# #   time.sleep(1)


# #如何连续调用多个装饰器:
# def add(func):
#     def inner():
#         x=func()
#         return x+1
#     return inner
# def cube(func):
#     def inner():
#         x=func()
#         return x*x*x
#     return inner
# def square(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner
# @add
# @cube
# @square
# def test():
#     return 2

# print(test())


#如何给装饰器传递参数
def outer(msg):
    def inner(func):
        print("inner里的msg：", msg)

        def ininner():
            print("开始执行")
            func()
            print("ininner里的msg：", msg)

        return ininner
    return inner


@outer(msg="结束执行")
def lucky():
    print("稍等片刻...")

lucky()




