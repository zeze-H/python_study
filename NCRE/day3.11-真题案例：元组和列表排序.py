# 列表和元组
ls = [("苹果", 2), ("芒果", 4), ("草莓", 3), ("香蕉", 1)]
print(ls)

# 排序（按元组中第二个元素排序，降序）
ls.sort(key=lambda x: x[1], reverse=True)
print(ls)

for item in ls:
    # print(item[0] + ":" + str(item[1]))
    print("{}:{}".format(item[0], item[1]))
    
