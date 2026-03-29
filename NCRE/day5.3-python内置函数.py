# abs 求绝对值，如果是复数，返回复数的模：实部平方加虚部平方再开根号
a = -1
b = 2 + 5j
print(abs(a))
print(abs(b))

# divmod：求两数的商和余数
c = 5
d = 3
print(divmod(c, d))

# pow：x 的 y 次幂
print(pow(2, 3))

# round：四舍五入，可以指定保留小数位
print(round(5.23))

# 浮点数精度问题示例
print(round(5.2345, 3))

# all：所有元素为真或为空返回 True，否则 False
# any：只要有一个为真返回 True，空返回 False
ls = [1, 2, 3]
ls2 = []
ls3 = [1, 0, 1]

print(all(ls))   # 全为真
print(all(ls2))  # 空集
print(all(ls3))  # 有真有假

print(any(ls))   # 全为真
print(any(ls2))  # 空集
print(any(ls3))  # 有真有假

# reversed：返回一个逆序可迭代对象
v = [1, 2, 3, 4, 5]
print(reversed(v))
print(list(reversed(v)))

# sorted：将元素从小到大排序
m = [12, 45, 23, 46, 0]
print(sorted(m))

# sum：求和
print(sum(v))

# eval：执行表达式并返回结果
ls_str = "[1,2,3]"
print(type(ls_str))
print(type(eval(ls_str)))

# exec：执行任意 Python 语句（无返回值）
exec("a = 1 + 999")
print(a)

# range(a, b, s)：从 a 到 b（不含 b）以 s 为步长生成序列
for i in range(1, 10):
    print(i)
