# 递归: 函数自己调用自己。必须要有结束条件,否则会无限循环

# 错误示范: 没有结束条件,会一直打印直到报错
def funa():
    print("AWBDYL")
    funa()

# 正确示范: i 减到 0 就停
def funb(i):
    if i > 0:
        print("AWBDYL")
        funb(i - 1)
funb(10)


# ========== 阶乘: n! = 1*2*3*...*n ==========
# 迭代版:
def a(n):
    result = 1
    for i in range(1, n + 1):   # 1,2,3,...,n 逐个乘
        result *= i
    return result

# 递归版:
def b(n):
    if n == 1:          # 出口: 到 1 就返回 1
        return 1
    return n * b(n - 1) # 否则 = n 乘 上一层的答案

# b(4) 展开过程 (从里往外算):
#   b(1)          -> 1
#   b(2) = 2 * 1  -> 2
#   b(3) = 3 * 2  -> 6
#   b(4) = 4 * 6  -> 24
print(a(4))   # 24
print(b(4))   # 24


# 斐波那契数列
#迭代:
def fibiter(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b
        a = b
        b = c
        n -=1
    return c
# 递归:
def fibrecur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibrecur(n-1)+fibrecur(n-2)
