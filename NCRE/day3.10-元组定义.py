# 元组：有序不可变：tuple
x = (123, 666, "中国人", "abc", "hello")
print(x)
print(type(x))

# 不支持删除，但支持索引取值
print(x[0])
print(x[1])

# 支持切片
print(x[::-1])
print(x[0:4:2])
