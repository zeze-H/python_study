s = {12, 13, 14, 15, 16, 89, 75}
print(len(s))  # 查看集合有多少个元素
print(12 in s)
print(122 not in s)

# 添加：add
s.add("中国移动")
print(s)

# 移除，如果不存在则会报错：remove
s.remove("中国移动")
print(s)

# 移除，不存在不会报错：discard
s.discard("中国移动")
print(s)

# 移除：pop
# 集合中 pop() 不能指定元素，只能随机弹出一个元素
s.pop()
print(s)

# 清空集合
s.clear()
print(s)

# 定义空集合
m = {}  # 什么都没有的时候是字典
print(m)
print(type(m))

m = {11, 12}
print(m)
print(type(m))

m = set()
print(m)
print(type(m))

m = set({})
print(m)
print(type(m))
