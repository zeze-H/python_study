# 创建空列表
ls = []
# ls = list()
# ls = list([])  # 修正拼写错误
print(type(ls))

# 在列表末尾添加元素：append
ls.append(123)
ls.append("abc")
print(ls)

# 指定位置添加元素：insert
ls.insert(1, "hello")
print(ls)

# 修改某个位置的元素
ls[0] = "你好"
ls[1] = "你好"
print(ls)

# 删除某个位置的元素：pop（默认删除最后一个，也可以指定位置删除）
ls.pop(2)
print(ls)

# 删除某个指定内容的元素：remove
ls.remove("你好")
print(ls)

# 清空列表
ls.clear()
print(ls)

# 拷贝列表：copy（浅拷贝）
# 将原列表拷贝，复制之后如果修改新列表，原列表不会改变（copy情况）
a = [123, 234, 567]
b = a  # 赋值引用，同一个对象
b[0] = "zeze"
print(a)

c = a.copy()  # 创建新列表
c[0] = "huanhuan"
print(a)
print(b)
print(c)
