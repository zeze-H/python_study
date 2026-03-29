'''
d = {}

# 根据键取值，自定义找不到的返回值
n = d.get("苹果", 0) + 1
print(n)

# 修改值
d["苹果"] = n
print(d)

# 将原先的苹果1再修改一次
d["苹果"] = n = d.get("苹果", 0) + 1
print(d)
'''

'''
ls = ["苹果", "苹果", "苹果", "芒果"]
for item in ls:
    print(item)
'''

# 统计列表中元素出现次数
'''
ls = ["苹果", "苹果", "苹果", "芒果"]
d = {}
for item in ls:
    d[item] = d.get(item, 0) + 1
    print(item)
    print(d)
'''

'''
ls = ["苹果", "香蕉", "香蕉", "芒果", "香蕉", "香蕉", "芒果", "芒果", "苹果", "苹果"]
d = {}
for item in ls:
    d[item] = d.get(item, 0) + 1
    print(item)

print(d)

# 将整理过后的字典，转换成列表然后进行排序
items_list = list(d.items())
print("排序前：", items_list)

# 对列表内的元组进行排序
items_list.sort(key=lambda x: x[1], reverse=True)
print("排序后：", items_list)

# 遍历列表，然后格式化输出
for item in items_list:
    print("{}:{}".format(item[0], item[1]))
'''

s = "苹果 香蕉 香蕉 芒果 香蕉 香蕉 芒果 芒果 苹果 苹果"

# 切割字符串左右两边空格，然后再分割，可以将字符串转换为列表
ls = s.strip().split()
print(ls)

d = {}
for item in ls:
    d[item] = d.get(item, 0) + 1

print(d)

# 将整理过后的字典，转换成列表然后进行排序
items_list = list(d.items())
print("排序前：", items_list)

# 对列表内的元组进行排序
items_list.sort(key=lambda x: x[1], reverse=True)
print("排序后：", items_list)

# 遍历列表，然后格式化输出
for item in items_list:
    print("{}:{}".format(item[0], item[1]))
