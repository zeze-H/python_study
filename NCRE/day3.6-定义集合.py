# 组合数据类型：集合、列表、元组、字典

# 集合类型：set，无序，支持元素去重
s = {123, 123, "hello", 3.14, "你好"}
print(s)
print(len(s))
print(type(s))

# 定义集合
set_a = {1, 2, 3, 4, 5, 6, 7}
set_b = {1, 2, 3, 4, 5, 6, 8}
print(set_a)
print(set_b)

# 并集
print("并集", set_a | set_b)

# 差集：set_a 有，set_b 没有的
print("差集", set_a - set_b)

# 交集
print("交集", set_a & set_b)

# 补集：也叫对称差集，就是 set_a 和 set_b 中只属于其中一个集合的元素
print("补集", set_a ^ set_b)
