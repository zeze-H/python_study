d = {"001": "张三", "002": "李四", "003": "王五"}

print(len(d))
print(max(d))
print(min(d))

# 判断是否存在，只能用键 keys 不能用值 values
print("002" in d)
print("002" not in d)
print("005" in d)

# 常用操作方法
d = {"001": "张三", "002": "李四", "003": "王五"}

# 取键
print(d.keys())

# 取值
print(d.values())

# 取键值对（返回元组）
print(d.items())

# 遍历字典的键、值、键值对
for key in d.keys():
    print(key)

for value in d.values():
    print(value)

# 遍历键值对（元组）
for item in d.items():
    print(item)

# 排序：将元组转换为列表（列表有序可变）
items_list = list(d.items())
print("排序前：", items_list)

items_list.sort(key=lambda x: x[1], reverse=True)
print("排序后：", items_list)

# 根据键 key 取值 value
# 如果不存在会报错
print(d["001"])

d["004"] = "zeze"
print(d)

# get 根据键取值，如果没有就会返回 None，也可以自定义返回值
print(d.get("005"))
print(d.get("005", 0))
