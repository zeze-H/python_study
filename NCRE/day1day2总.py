'''Day 1'''

# 二进制
print(0b1010)
print(0B1010)

# 八进制
print(0o1010)
print(0O1010)

# 十六进制
print(0x1010)
print(0X1010)

# 十进制
print(1010)
print(1010)

# print函数默认会把各种进制转换成十进制

f = 1.25
print(type(f))

# e4、E5 分别代表乘以10的几次方
print(2.01e4)
print(-3.2e5)

# 复数类型 a+bj
a = 18 + 5j

# 获取实部
print(a.real)

# 获取虚部
print(a.imag)

# 默认浮点类型
print(type(a.imag))

# type函数
a = 124  # int
b = 23.5  # float
print(type(a))
print(type(b))

c = 5 + 6.7j  # complex
d = "hello world"  # str
e = False  # bool
print(type(c))
print(type(d))
print(type(e))

f = [1, 2, 3, 4]  # list
g = (1, 2, 3, 4)  # tuple
h = {1, 2, 3, 4}  # set
i = {"1": "2", "3": "4"}

print(type(f))
print(type(g))
print(type(h))

'''运算符'''

# 算数运算符
x = 10
y = 4
z = 3
c = 2

print(x + y)  # 加
print(x - y)  # 减
print(x * y)  # 乘
print(x / y)  # 除
print(x // y)  # 整除
print(x % y)  # 取余数
print(c ** y)  # 幂运算
print(10 % 2 == 0)  # 判断偶数

# 逻辑运算符
a = 4
b = 5

# 必须全是 True 才是 True
print(a > b and b == 5)

# 只要有一个是 True 就可以
print(a > b or b == 5)

# 取反
print(not b == 5)

'''Day2'''

# 程序控制的三种结构：顺序结构、分支结构 if-elif-else、循环结构 for-while

# 银行自助取款机程序
balance = 3000
money = eval(input("请输入你要取多少钱："))

if money <= balance and money % 100 == 0:
    balance -= money
    print("正在出钞...")
    print("取钱成功，你的余额是:", balance, "元")
else:
    print("余额不足!或输入的不是整百面值")

# if-elif-else:
# 90及以上优秀，80及以上良好，60及以上及格，60及以下不合格
score = eval(input("请输入你的分数："))

if score >= 90:
    print("优秀！！！")
elif score >= 80:
    print("良好!")
elif score >= 60:
    print("及格")
else:
    print("不及格！")

# 语句嵌套：
password = int(input("请输入密码："))

if password == 111111:
    balance = 3000
    money = int(input("请输入要取的钱数："))
    if money <= balance:
        if money % 100 == 0:
            balance -= money
            print("正在准备出钞")
            print("取钱成功 余额还有：", balance)
        else:
            print("取现失败，请输入整百！")
    else:
        print("余额不足")
else:
    print("密码错误！！！")

# 真题示例：
n = eval(input("请输入数量："))

if n >= 10:
    cost = 150 * n * 0.7
elif n >= 4:
    cost = 150 * n * 0.8
elif n >= 2:
    cost = 150 * n * 0.9
else:
    cost = 150 * n

cost = int(cost)
print("总额为：", cost)

# 循环结构：for、while
n = 0
while n < 10:
    print("zezeHUAN")
    n += 1

x = 1
while x <= 10:
    print(x)
    x += 1

y = 0
while y < 10:
    y += 1
    print(y)

# 计算1-100之间的数之和：while-else
i = 1
num = 0

while i <= 100:
    print(i)
    num += i
    i += 1
else:
    print("while结束")

print("和为：", num)

# 循环控制：continue：用来结束本次循环，直接重新循环
# 用while只打印偶数，不打印奇数
i = 1
while i <= 100:
    i += 1
    if i % 2 == 0:
        print(i)

print("偶数程序结束")

# 利用continue反转，打印奇数
i = 1
while i <= 100:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

print("奇数程序结束")

# break：直接退出此次循环
# 打印100之间的偶数的前十个
i = 1
n = 0
while i <= 100:
    i += 1
    if i % 2 == 0:
        print(i)
        n += 1
    if n == 10:
        break

# 游戏：猜猜我是谁
import random

# 每次运行会得到1到10之间的随机数
target = random.randint(1, 10)

# 用户输入数字：None表示常量，无值
'''guss = None
while target != guss:
    guss = int(input("猜猜我是谁："))
    if guss > target:
        print("大了")
    if guss < target:
        print("小了")
    else:
        print("正确！！！")
        break
'''

'''处理异常'''

try:
    score = float(input("请输入分数："))
    print("你的分数是：", score)
except:
    print("请输入数字!")

print("这是正常代码，会被执行")

# 处理单独具体异常：程序的健壮性
try:
    score = float(input("请输入分数："))
    print("你的分数是：", score)
except ValueError:
    print("你输入的不是数字，请输入数字！")
except ZeroDivisionError:
    print("0不能做除数")
except:
    print("程序出错了！")

print("这是正常代码，会被执行")

# 字符串的切片：
s = "你好我叫泽泽呀"
print(len(s))
print(s[0:4])
print(s[1:4])
print(s[0:4:1])
print(s[0:4:2])
print(s[:4])
print(s[:])
print(s[::])
print(s[::-1])
print(s[:-1])
print(s[:-2:-1])
