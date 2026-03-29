# 以下处理办法只是处理副本，并不会影响原始数据

# 字符串的切割：split，并且返回列表
'''
s = "are-you-ok-?"
s2 = s.split("-")
print(s2)
print(type(s2))

name = "刘备 关羽 张飞"
names = name.split(" ")
print(names)
'''

# 字符串的替换：replace
'''
s = "are-you-ok-?"
print(s.replace("are", "ARE"))
print(s.replace("-", " "))
print(s)
'''

# strip：删除字符串左右两边的空格或指定字符
'''
s1 = "   are   "
print(s1)
print(s1.strip())

s2 = "**are**"
print(s2.strip("*"))
'''

# 将可迭代对象（其中元素必须都是字符串）中的所有元素，
# 用 join 指定的字符串作为分隔符连接起来，并返回新的字符串
'''
print(",".join("pyhon"))
l = ["are", "you", "ok", "?"]
s = "".join(l)
print(s)
print(type(s))
'''

# lower：字符串副本全变为小写
# upper：字符串副本全变为大写
'''
s1 = "ARE YOU OK?"
s2 = "are you ok?"
s3 = s1.lower()
s4 = s2.upper()
print(s3)
print(s4)
print(type(s3))
print(type(s4))
'''

# 查找指定字符出现次数：count
'''
s = "are-you-ok-?are-you-ok-?are-you-ok-?are-you-ok-?"
print(s.count("are"))
'''

# 字符串居中函数：center，不足指定位数默认空格填充，也可以指定填充字符
'''
s = "are"
print(s.center(10))
print(s.center(10, "*"))

# 超过指定位数，原封不动直接打印
print(s.center(1))
'''

# 首字母大写：capitalize
'''
s = "are you ok?"
print(s.capitalize())
'''

# 查找指定字符串第一次出现的位置下标，支持指定下标范围
'''
s = "are you ok?are you ok?are you ok?"
print(len(s))
print(s.find("ok"))
print(s.find("ok", 10, 30))
print(s.rfind("ok"))

# 如果找不到，find 会返回 -1，而 index 会直接报错
print(s.index("ok"))
print(s.index("ok", 10, 30))
'''
