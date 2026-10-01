# ========== 生成器基础: counter ==========
def counter():
    i = 0
    while i < 5:
        yield i
        # yield 会暂停函数并保存当前状态(包括局部变量),
        # 下次调用 next() 时从暂停处继续执行
        i += 1

# 生成器是一种特殊的迭代器,支持内置函数 next()
c = counter()
print(next(c))  # 0
print(next(c))  # 1
print(next(c))  # 2
print(next(c))  # 3
print(next(c))  # 4

# 数据全部产出后,再次调用 next() 会抛出 StopIteration 异常
try:
    print(next(c))
except StopIteration:
    print("生成结束,触发 StopIteration")


# ========== 生成器: 斐波那契数列 (除前两项 0,1 外, 后一项 = 前两项之和) ==========
def fibonacci(n):
    # 生成前 n 个斐波那契数
    a, b = 0, 1              # a=当前项(0), b=下一项(1)
    for _ in range(n):
        yield a              # 产出当前项,并暂停
        a, b = b, a + b      # 挪一格: 新a=旧b(当前项), 新b=旧a+旧b(前两项之和)

# 用 for 循环逐个取
for num in fibonacci(10):
    print(num, end=" ")      # 0 1 1 2 3 5 8 13 21 34
print()


# ========== 生成器表达式 vs 列表推导式 ==========
# 生成器表达式: 用 (), 不会立刻算, 返回一个生成器对象, 用一个算一个(省内存)
gen = (i ** 2 for i in range(10))
print(gen)            # <generator object ...> 打印的是对象本身,不是数据
print(next(gen))      # 0  取第一个值
print(next(gen))      # 1  接着从暂停处取下一个
for i in gen:         # 剩下的接着取
    print(i)          # 4 9 16 25 36 49 64 81
# 注意: 生成器只能遍历一次, 上面取完后再遍历就是空的

# 列表推导式: 用 [], 立刻把所有数据算出来存进列表(占内存), 但可反复使用
lst = [i ** 2 for i in range(10)]
print(lst)            # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(lst)            # 可以再打印一遍, 内容还在